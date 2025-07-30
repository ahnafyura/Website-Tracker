# search_web.py
from googlesearch import search
from config import SEARCH_LANGUAGE, NUM_SEARCH_RESULTS

def find_related_sites(query):
    results = []
    try:
        # Perubahan: gunakan 'num_results' bukan 'num'
        for url in search(query, num_results=NUM_SEARCH_RESULTS, lang=SEARCH_LANGUAGE):
            results.append(url)
    except Exception as e:
        print(f"Terjadi error saat pencarian: {e}")
    return results

if __name__ == "__main__":
    print(find_related_sites("AI-powered customer support site"))
