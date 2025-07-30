# chunker.py
from config import CHUNK_SIZE

def chunk_text(text, max_words=CHUNK_SIZE):
    words = text.split()
    chunks = [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
    return chunks

if __name__ == "__main__":
    sample_text = "This is an example text " * 50
    print(chunk_text(sample_text))
