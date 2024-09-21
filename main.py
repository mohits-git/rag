import pymongo
import requests

from config import DATABASE_URI, EMBEDDING_URL, HF_ACCESS_TOKEN

client = pymongo.MongoClient(DATABASE_URI)
db = client.sample_mflix
collection = db.movies


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        EMBEDDING_URL,
        headers={"Authorization": f"Bearer {HF_ACCESS_TOKEN}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise Exception(
            f"Request failed with status code: {
                response.status_code}, {response.text}"
        )

    return response.json()


def create_plot_embeddings():
    for doc in collection.find({'plot': {"$exists": True}}).limit(50):
        doc['plot_embedding'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)


def query_plot(query: str):
    results = collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": generate_embedding(query),
                "path": "plot_embedding",
                "numCandidates": 100,
                "limit": 4,
                "index": "PlotSemanticSearch"
            },
        },
    ])
    for doc in results:
        print(f"Movie Name: {doc['title']}, \nMovie Plot: {doc['plot']}\n")


query_plot("imaginary characters from outer space at war")
