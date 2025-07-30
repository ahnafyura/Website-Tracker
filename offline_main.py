import numpy as np
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from search_web import find_related_sites
from scraper import scrape_website
from chunker import chunk_text
from analyzer import analyze_websites

def main():
    query = input("Masukkan keyword pencarian website: ").strip()
    if not query:
        print("[-] Keyword tidak boleh kosong.")
        return

    urls = find_related_sites(query)
    print("Ditemukan website:", urls)

    metadata = []
    for url in urls:
        print(f"\n[+] Scraping: {url}")
        text = scrape_website(url)
        if not text:
            print("[-] Tidak ada teks diambil.")
            continue

        chunks = chunk_text(text)
        for chunk in chunks:
            metadata.append({"url": url, "chunk_text": chunk})

    if not metadata:
        print("[-] Tidak ada data yang bisa diproses.")
        return

    report = analyze_websites(metadata)

    # Save to Excel
    df = pd.DataFrame(report)
    df.to_excel("output_websites.xlsx", index=False)

    print("\n=== LAPORAN ANALISIS ===")
    print(df)

if __name__ == "__main__":
    main()