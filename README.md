# Website Scraper & Analyzer (Python)

## 📌 Project Description__

This project is a **Python-based Web Scraping and Analysis Tool** designed to automatically search, scrape, and analyze website content based on a given keyword query. The project supports two operational modes:

1. **Online Mode (OpenAI API)** – Uses AI embeddings for advanced text analysis.
2. **Offline Mode (TF-IDF)** – Uses traditional keyword extraction for analysis without relying on API credits.

All results are **exported into an Excel file**, providing a structured, easy-to-read report with top keywords and word counts from the scraped pages.

---

## 📂 Directory Structure

```
website_scraper/
│
├── config.py           # Configuration variables
├── search_web.py       # Finds related websites from Google Search
├── scraper.py          # Extracts text from target websites
├── chunker.py          # Splits text into chunks for processing
├── embedder.py         # Handles embeddings (OpenAI API)
├── analyzer.py         # Analyzes text using TF-IDF or AI embeddings
├── database_manager.py # Manages FAISS database for vector storage
├── online_main.py      # Runs full pipeline using OpenAI API
├── offline_main.py     # Runs full pipeline using TF-IDF analysis
├── main.py             # Auto-detects mode (online/offline)
├── requirements.txt    # Required Python packages
└── README.md           # Documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/website_scraper.git
cd website_scraper
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Set up your OpenAI API key:

```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

If no API key is found, the project automatically switches to **offline mode**.

---

## 🚀 Usage

Run the project:

```bash
python main.py
```

### Workflow:

1. Enter a search keyword (e.g., `AI in manufacturing industry`).
2. The system retrieves relevant websites via Google Search.
3. Each website is scraped for text content.
4. Text data is split into smaller chunks for analysis.
5. **Online Mode** → Uses OpenAI embeddings to process text.
6. **Offline Mode** → Uses TF-IDF for keyword extraction.
7. Results are saved into `output_websites.xlsx`.

---

## 📊 Output Example

| URL                                                                    | Word Count | Top Keywords                  |
| ---------------------------------------------------------------------- | ---------- | ----------------------------- |
| [https://www.ibm.com/think/topics](https://www.ibm.com/think/topics)   | 1584       | ai, manufacturing, automation |
| [https://www.autodesk.com/articles](https://www.autodesk.com/articles) | 1342       | robotics, ai, industry        |

The Excel file will be generated automatically in the project folder.

---

## 🛠 Technical Documentation

### 1️⃣ `search_web.py`

* Uses `googlesearch` or `requests` to fetch top websites related to the keyword.
* Configurable for number of results and language.

### 2️⃣ `scraper.py`

* Extracts visible text from `<p>` tags.
* Cleans whitespace and HTML artifacts.

### 3️⃣ `chunker.py`

* Splits long text into smaller, manageable pieces (default: 300 words).

### 4️⃣ `embedder.py`

* Generates text embeddings using OpenAI API (`text-embedding-ada-002`).
* Used only in online mode.

### 5️⃣ `analyzer.py`

* Offline: Uses TF-IDF (`sklearn`) to extract top keywords.
* Online: Uses semantic similarity and embeddings for clustering keywords.

### 6️⃣ `database_manager.py`

* Stores embeddings in a FAISS vector database for similarity searches.

### 7️⃣ `main.py`

* Auto-selects mode based on presence of `OPENAI_API_KEY`.
* Handles pipeline execution and Excel export.

---

## 📜 License

This project is licensed under the MIT License – you are free to use, modify, and distribute it with proper attribution.

---

## 🤝 Contributing

Pull requests are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Submit a pull request

---

## 💡 Future Enhancements

* Add multi-language support for text analysis
* Implement content summarization per website
* Build a simple web UI for non-technical users
