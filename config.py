from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.environ["DATABASE_URL"]
HF_ACCESS_TOKEN = os.environ["HF_ACCESS_TOKEN"]
EMBEDDING_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
