from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_websites(metadata):
    report = []
    docs = [m["chunk_text"] for m in metadata]

    # TF-IDF keyword extraction
    vectorizer = TfidfVectorizer(max_features=10, stop_words='english')
    X = vectorizer.fit_transform(docs)
    keywords = vectorizer.get_feature_names_out()

    for idx, data in enumerate(metadata):
        words = re.findall(r'\w+', data["chunk_text"])
        wc = len(words)
        report.append({
            "url": data["url"],
            "word_count": wc,
            "top_keywords": ", ".join(keywords)
        })
    return report