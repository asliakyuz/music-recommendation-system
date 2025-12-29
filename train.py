import pandas as pd
import numpy as np
import pickle
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# Klasör oluştur
os.makedirs("models", exist_ok=True)

SEQ_LEN = 3

# =========================
# 1. VERİLER
# =========================
print("Users.csv okunuyor...")
users = pd.read_csv("data/users.csv")
print("Toplam kullanıcı sayısı:", len(users))

print("\nArtist verisi okunuyor...")
artists = pd.read_csv(
    "data/user_top_artists.csv",
    usecols=["user_id", "artist_name", "playcount"],
    nrows=5000
)
artists["artist_name"] = artists["artist_name"].str.lower()

print("\nAlbum verisi okunuyor...")
albums = pd.read_csv(
    "data/user_top_albums.csv",
    usecols=["user_id", "album_name", "playcount"],
    nrows=5000
)
albums["album_name"] = albums["album_name"].str.lower()

# =========================
# 2. ENCODING
# =========================
le_artist = LabelEncoder()
artists["artist_id"] = le_artist.fit_transform(artists["artist_name"])

le_album = LabelEncoder()
albums["album_id"] = le_album.fit_transform(albums["album_name"])

# =========================
# 3. SEQUENCE OLUŞTURMA
# =========================
def create_sequences(df, col_name):
    sorted_df = df.sort_values(by=["user_id","playcount"], ascending=[True, False])
    user_seq = sorted_df.groupby("user_id")[col_name].apply(list).reset_index()
    user_seq["len"] = user_seq[col_name].apply(len)
    user_seq = user_seq[user_seq["len"] >= 4]
    user_seq[col_name] = user_seq[col_name].apply(lambda x: x[:50])
    return user_seq

user_sequences_artist = create_sequences(artists, "artist_id")
user_sequences_album = create_sequences(albums, "album_id")

# =========================
# 4. X/Y OLUŞTURMA
# =========================
def create_xy(sequences, col_name):
    X, y = [], []
    for seq in sequences[col_name]:
        for i in range(len(seq)-SEQ_LEN):
            X.append(seq[i:i+SEQ_LEN])
            y.append(seq[i+SEQ_LEN])
    return np.array(X), np.array(y)

X_artist, y_artist = create_xy(user_sequences_artist, "artist_id")
X_album, y_album = create_xy(user_sequences_album, "album_id")

X_artist = pad_sequences(X_artist, maxlen=SEQ_LEN)
X_album = pad_sequences(X_album, maxlen=SEQ_LEN)

y_artist = to_categorical(y_artist, num_classes=len(le_artist.classes_))
y_album = to_categorical(y_album, num_classes=len(le_album.classes_))

# =========================
# 5. LSTM MODELİ
# =========================
def build_lstm_model(num_classes):
    model = Sequential()
    model.add(Embedding(input_dim=num_classes, output_dim=50, input_length=SEQ_LEN))
    model.add(LSTM(64))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# =========================
# 6. SANATÇI MODELİ
# =========================
print("\nSanatçı modeli eğitiliyor...")
X_train_a, X_test_a, y_train_a, y_test_a = train_test_split(X_artist, y_artist, test_size=0.2, random_state=42)
model_artist = build_lstm_model(len(le_artist.classes_))
model_artist.fit(X_train_a, y_train_a, epochs=5, batch_size=32, validation_split=0.1)
model_artist.save("models/model_artist.h5")

# =========================
# 7. ALBÜM MODELİ
# =========================
print("\nAlbüm modeli eğitiliyor...")
X_train_alb, X_test_alb, y_train_alb, y_test_alb = train_test_split(X_album, y_album, test_size=0.2, random_state=42)
model_album = build_lstm_model(len(le_album.classes_))
model_album.fit(X_train_alb, y_train_alb, epochs=5, batch_size=32, validation_split=0.1)
model_album.save("models/model_album.h5")

# =========================
# 8. ENCODER KAYDETME
# =========================
with open("models/encoder_artist.pkl", "wb") as f:
    pickle.dump(le_artist, f)
with open("models/encoder_album.pkl", "wb") as f:
    pickle.dump(le_album, f)

print("\nMODEL VE ENCODER KAYDEDİLDİ ✅")
