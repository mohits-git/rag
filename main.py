from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
MONGO_URI = os.environ["DATABASE_URL"]

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.sample_mflix
collection = db.movies

items = collection.find().limit(5)

for item in items:
    print(item)
