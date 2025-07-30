from openai import OpenAI
import time

client = OpenAI()

def embed_text(chunks):
    vectors = []
    for chunk in chunks:
        try:
            resp = client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            )
            vectors.append(resp.data[0].embedding)
        except Exception as e:
            if "insufficient_quota" in str(e):
                print("❌ ERROR: Kuota API habis atau tidak ada saldo di akun OpenAI Anda.")
                break
            else:
                print(f"[!] Embedding error pada chunk: {e}")
            time.sleep(1)
    return vectors
