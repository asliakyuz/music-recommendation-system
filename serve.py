import gradio as gr
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# =========================
# 1. MODELLERİ YÜKLE
# =========================
print("Modeller yükleniyor...")

model_artist = load_model("models/model_artist.h5")
model_album = load_model("models/model_album.h5")

with open("models/encoder_artist.pkl", "rb") as f:
    encoder_artist = pickle.load(f)
with open("models/encoder_album.pkl", "rb") as f:
    encoder_album = pickle.load(f)

print("Modeller hazır ✅")

SEQ_LEN = 3

# =========================
# ÖNERİ FONKSİYONLARI
# =========================
def recommend_artists(artist_input):
    try:
        artists = [a.strip().lower() for a in artist_input.split(",")]
        if len(artists) != SEQ_LEN:
            return f"Lütfen tam olarak {SEQ_LEN} sanatçı giriniz."
        unseen = [a for a in artists if a not in encoder_artist.classes_]
        if unseen:
            return f"Aşağıdaki sanatçılar eğitim verisinde yok: {', '.join(unseen)}"
        artist_ids = encoder_artist.transform(artists)
        artist_ids = np.array(artist_ids).reshape(1, SEQ_LEN)
        artist_ids = pad_sequences(artist_ids, maxlen=SEQ_LEN)
        probs = model_artist.predict(artist_ids)[0]
        top_ids = np.argsort(probs)[-5:][::-1]
        top_artists = encoder_artist.inverse_transform(top_ids)
        return "🎵 Sanatçı Önerileri:\n" + "\n".join([f"{i+1}. {a}" for i,a in enumerate(top_artists)])
    except Exception as e:
        return f"Hata: {str(e)}"

def recommend_albums(album_input):
    try:
        albums = [a.strip().lower() for a in album_input.split(",")]
        if len(albums) != SEQ_LEN:
            return f"Lütfen tam olarak {SEQ_LEN} albüm giriniz."
        unseen = [a for a in albums if a not in encoder_album.classes_]
        if unseen:
            return f"Aşağıdaki albümler eğitim verisinde yok: {', '.join(unseen)}"
        album_ids = encoder_album.transform(albums)
        album_ids = np.array(album_ids).reshape(1, SEQ_LEN)
        album_ids = pad_sequences(album_ids, maxlen=SEQ_LEN)
        probs = model_album.predict(album_ids)[0]
        top_ids = np.argsort(probs)[-5:][::-1]
        top_albums = encoder_album.inverse_transform(top_ids)
        return "💿 Albüm Önerileri:\n" + "\n".join([f"{i+1}. {a}" for i,a in enumerate(top_albums)])
    except Exception as e:
        return f"Hata: {str(e)}"

# =========================
# GRADIO ARAYÜZÜ
# =========================
artist_input = gr.Textbox(label="Son dinlenen 3 sanatçı", placeholder="radiohead, daft punk, coldplay")
album_input = gr.Textbox(label="Son dinlenen 3 albüm", placeholder="kid a, discovery, parachutes")

artist_examples = [
    ["radiohead, daft punk, coldplay"],
    ["ladytron, ghostface killah, unkle"],
    ["crystal castles, radiohead, daft punk"],
    ["nine inch nails, daft punk, radiohead"]
]

album_examples = [
    ["kid a, discovery, back to black"],
    ["silent shout, grace, ok computer"],
    ["in rainbows, homework, abbey road"],
    ["ok computer, kid a, discovery"]
]

examples = [[a[0], b[0]] for a,b in zip(artist_examples, album_examples)]

interface = gr.Interface(
    fn=lambda a,b: (recommend_artists(a), recommend_albums(b)),
    inputs=[artist_input, album_input],
    outputs=["text","text"],
    examples=examples,
    title="Müzik Öneri Sistemi 🎵",
    description="Son 3 dinlenen sanatçı ve albüme göre Top-5 önerir."
)

if __name__ == "__main__":
    interface.launch(share=True)
