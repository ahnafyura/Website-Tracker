import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Google Search
SEARCH_LANGUAGE = "en"
NUM_SEARCH_RESULTS = 5

# Scraper
REQUEST_TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (compatible; WebsiteTrackerBot/1.0)"

# Chunking
CHUNK_SIZE = 300  # jumlah kata per chunk

# FAISS database
VECTOR_DIM = 1536  # dimensi text-embedding-ada-002
FAISS_INDEX_FILE = "website_index.faiss"
METADATA_FILE = "metadata.json"

# Mode (auto-detect)
USE_OPENAI = bool(OPENAI_API_KEY)