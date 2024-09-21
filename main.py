import pymongo
import requests

from config import DATABASE_URI, HF_ACCESS_TOKEN

client = pymongo.MongoClient(DATABASE_URI)
db = client.sample_mflix
collection = db.movies


embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {HF_ACCESS_TOKEN}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise Exception(
            f"Request failed with status code: {
                response.status_code}, {response.text}"
        )

    return response.json()


print(generate_embedding("Hello, World!"))
