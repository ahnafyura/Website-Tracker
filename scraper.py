import requests
from bs4 import BeautifulSoup
from config import REQUEST_TIMEOUT, USER_AGENT
import re

headers = {"User-Agent": USER_AGENT}

def scrape_website(url):
    # Skip jika URL tidak valid
    if not url.startswith("http"):
        print(f"[!] URL dilewati karena tidak valid: {url}")
        return ""

    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text(separator=" ", strip=True) for p in soup.find_all('p')]
        text = ' '.join(paragraphs)
        clean_text = re.sub(r'\s+', ' ', text)
        return clean_text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
