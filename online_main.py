import numpy as np
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from search_web import find_related_sites
from scraper import scrape_website
from chunker import chunk_text
from embedder import embed_text
from database_manager import create_index, save_metadata
from analyzer import analyze_websites

OUTPUT_EXCEL = "hasil_tracking_website.xlsx"

def main():
    query = input("Masukkan keyword pencarian website: ").strip()
    if not query:
        print("[-] Keyword tidak boleh kosong.")
        return

    urls = find_related_sites(query)
    urls = [u for u in urls if u.startswith("http")]
    print("Ditemukan website:", urls)

    all_vectors = []
    metadata = []

    for url in urls:
        print(f"\n[+] Scraping: {url}")
        text = scrape_website(url)

        if not text or len(text.strip()) == 0:
            print(f"[-] Tidak ada teks yang dapat diambil dari {url}")
            continue

        # Chunking
        chunks = chunk_text(text)
        if not chunks:
            print("[-] Tidak ada chunk yang dihasilkan.")
            continue

        # Embedding
        try:
            vectors = embed_text(chunks)
        except Exception as e:
            if "insufficient_quota" in str(e).lower():
                print("❌ Kuota API OpenAI habis, hentikan proses embedding.")
                break
            else:
                print(f"[!] Gagal embedding untuk {url}: {e}")
                continue

        if isinstance(vectors, np.ndarray) and vectors.size > 0:
            all_vectors.append(vectors)
            for chunk in chunks:
                metadata.append({
                    "url": url,
                    "chunk_text": chunk
                })
        else:
            print("[-] Embedding kosong atau gagal.")

    if all_vectors:
        combined_vectors = np.vstack(all_vectors)
        create_index(combined_vectors)
        save_metadata(metadata)
        print("\n[✔] Data berhasil disimpan ke FAISS.")

        # Analisis
        report = analyze_websites(metadata)
        print("\n=== LAPORAN ANALISIS ===")
        for r in report:
            print(f"- {r['url']}")
            print(f"  Jumlah kata: {r['word_count']}")
            print(f"  Top keywords: {r['top_keywords']}")

        # === Simpan ke Excel ===
        df_meta = pd.DataFrame(metadata)
        df_report = pd.DataFrame(report)

        with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
            df_meta.to_excel(writer, sheet_name="Metadata", index=False)
            df_report.to_excel(writer, sheet_name="Analisis", index=False)

        print(f"\n[📂] Hasil berhasil diekspor ke file: {OUTPUT_EXCEL}")

    else:
        print("[-] Tidak ada data yang bisa diproses.")

if __name__ == "__main__":
    main()
