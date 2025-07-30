import os
from openai import OpenAI
from dotenv import load_dotenv

# Paksa membaca file .env di direktori yang sama
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API Key tidak ditemukan. Pastikan file .env berada di folder yang sama dengan script ini.")
else:
    print("✅ API Key ditemukan:", api_key[:10] + "..." if api_key else "Tidak ada")

    try:
        client = OpenAI(api_key=api_key)
        response = client.models.list()
        print("✅ Berhasil terhubung ke OpenAI API.")
        print("   Jumlah model tersedia:", len(response.data))
    except Exception as e:
        print("❌ Gagal terhubung ke OpenAI API:", e)
