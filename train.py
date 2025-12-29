import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# =========================
# 1. USERS
# =========================
print("Users.csv okunuyor...")
users = pd.read_csv("data/users.csv")
print("Toplam kullanıcı sayısı:", len(users))

# =========================
# 2. ARTIST VERİSİ
# =========================
print("\nArtist verisi okunuyor...")
artists = pd.read_csv(
    "data/user_top_artists.csv",
    usecols=["user_id", "artist_name", "playcount"],
    nrows=20000  
)

# Harf hassasiyeti kaldırıldı
artists["artist_name"] = artists["artist_name"].str.lower()

print("Artist veri boyutu:", artists.shape)
print(artists.head())

# =========================
# 3. ALBUM VERİSİ
# =========================
print("\nAlbum verisi okunuyor...")
albums = pd.read_csv(
    "data/user_top_albums.csv",
    usecols=["user_id", "album_name", "playcount"],
    nrows=20000
)

# Harf hassasiyeti kaldırıldı
albums["album_name"] = albums["album_name"].str.lower()

print("Album veri boyutu:", albums.shape)
print(albums.head())

# =========================
# 4. ENCODING
# =========================
print("\nSanatçı encoding yapılıyor...")
le_artist = LabelEncoder()
artists["artist_id"] = le_artist.fit_transform(artists["artist_name"])
print("Encode edilen sanatçı sayısı:", len(le_artist.classes_))

print("\nAlbüm encoding yapılıyor...")
le_album = LabelEncoder()
albums["album_id"] = le_album.fit_transform(albums["album_name"])
print("Encode edilen albüm sayısı:", len(le_album.classes_))

# =========================
# 5. SEQUENCE OLUŞTURMA
# =========================
SEQ_LEN = 3

def create_sequences(df, col_name):
    sorted_df = df.sort_values(by=["user_id","playcount"], ascending=[True, False])
    user_seq = sorted_df.groupby("user_id")[col_name].apply(list).reset_index()
    user_seq["len"] = user_seq[col_name].apply(len)
    user_seq = user_seq[user_seq["len"] >= 4]
    user_seq[col_name] = user_seq[col_name].apply(lambda x: x[:50])
    return user_seq

print("\nKullanıcı bazlı sequence oluşturuluyor (sanatçı)...")
user_sequences_artist = create_sequences(artists, "artist_id")
print("Sanatçı sequence sayısı:", len(user_sequences_artist))

print("\nKullanıcı bazlı sequence oluşturuluyor (albüm)...")
user_sequences_album = create_sequences(albums, "album_id")
print("Albüm sequence sayısı:", len(user_sequences_album))

# =========================
# 6. X/y
# =========================
def create_xy(sequences, col_name):
    X, y = [], []
    for seq in sequences[col_name]:
        for i in range(len(seq)-SEQ_LEN):
            X.append(seq[i:i+SEQ_LEN])
            y.append(seq[i+SEQ_LEN])
    return np.array(X), np.array(y)

print("\nX/y oluşturuluyor (sanatçı)...")
X_artist, y_artist = create_xy(user_sequences_artist, "artist_id")
print("Sanatçı toplam örnek sayısı:", len(X_artist))

print("\nX/y oluşturuluyor (albüm)...")
X_album, y_album = create_xy(user_sequences_album, "album_id")
print("Albüm toplam örnek sayısı:", len(X_album))

# =========================
# 7. MODEL EĞİTİMİ
# =========================
print("\nSanatçı modeli eğitiliyor...")
X_train_a, X_test_a, y_train_a, y_test_a = train_test_split(X_artist, y_artist, test_size=0.2, random_state=42)
model_artist = LogisticRegression(max_iter=500, n_jobs=-1)
model_artist.fit(X_train_a, y_train_a)
y_pred_a = model_artist.predict(X_test_a)
acc_artist = accuracy_score(y_test_a, y_pred_a)
print(f"Sanatçı model doğruluğu: %{acc_artist*100:.2f}")

print("\nAlbüm modeli eğitiliyor...")
X_train_alb, X_test_alb, y_train_alb, y_test_alb = train_test_split(X_album, y_album, test_size=0.2, random_state=42)
model_album = LogisticRegression(max_iter=500, n_jobs=-1)
model_album.fit(X_train_alb, y_train_alb)
y_pred_alb = model_album.predict(X_test_alb)
acc_album = accuracy_score(y_test_alb, y_pred_alb)
print(f"Albüm model doğruluğu: %{acc_album*100:.2f}")

# =========================
# 8. KAYDETME
# =========================
print("\nModel ve encoder kaydediliyor...")
with open("models/model_artist.pkl", "wb") as f:
    pickle.dump(model_artist, f)
with open("models/model_album.pkl", "wb") as f:
    pickle.dump(model_album, f)
with open("models/encoder_artist.pkl", "wb") as f:
    pickle.dump(le_artist, f)
with open("models/encoder_album.pkl", "wb") as f:
    pickle.dump(le_album, f)

print("\nMODEL KAYDEDİLDİ ✅")
