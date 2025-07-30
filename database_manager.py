import faiss
import json
import numpy as np
import os
from config import FAISS_INDEX_FILE, METADATA_FILE

def create_index(vectors):
    """
    Membuat index FAISS dari embedding vectors dan menyimpannya ke file.
    """
    if vectors is None or len(vectors) == 0:
        raise ValueError("Tidak ada vektor yang dapat disimpan ke FAISS.")

    # Deteksi dimensi otomatis
    vector_dim = vectors.shape[1]
    index = faiss.IndexFlatL2(vector_dim)
    index.add(vectors)
    faiss.write_index(index, FAISS_INDEX_FILE)
    print(f"[✔] Index FAISS dibuat dengan {vectors.shape[0]} vektor (dimensi: {vector_dim}).")

def load_index():
    """
    Memuat index FAISS jika ada.
    """
    if not os.path.exists(FAISS_INDEX_FILE):
        print("[-] File index FAISS tidak ditemukan.")
        return None
    return faiss.read_index(FAISS_INDEX_FILE)

def save_metadata(metadata):
    """
    Menyimpan metadata ke file JSON.
    """
    if not metadata:
        print("[-] Tidak ada metadata yang dapat disimpan.")
        return
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    print(f"[✔] Metadata berhasil disimpan ({len(metadata)} entri).")

def load_metadata():
    """
    Memuat metadata dari file JSON jika ada.
    """
    if not os.path.exists(METADATA_FILE):
        print("[-] File metadata tidak ditemukan.")
        return []
    try:
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[-] Metadata corrupt atau kosong.")
        return []
