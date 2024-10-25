# Rag QA app
- Ask questions to your documents.
- Implemented with
  - OpenAI APIs (to generate embeddings and text generation)
  - MongoDB Atlas Vector (for vector store, vector search)
- UI built with Gradio.

## Get Started
- Clone Repo:
```bash
git clone https://github.com/mohits-git/rag
```
- Move to correct project director
```bash
cd rag/rag-qa
```
- Create a virtual environment
```bash
python3 -m venv venv
```
- Activate the virtual environment
```bash
source venv/bin/activate
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Add Environment variables in `.env` (refer `.env.example`
```bash
OPENAI_API_KEY=
# Your MongoDB Atlas connection string
DATABASE_URL=
```
- *(Optional)* Add your documents (.txt) in the `sample_files` folder
- Load Your documents data, generate vector embeddings via OpenAI Embedding modal and store in MongoDB Atlas
```bash
python3 load_data.py
```
- Go to cloud.mongodb.com > your_project > your_cluster > browse collections. You can see a new db with a collction having `text` and their `embedding`
```
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
```
- Now create a new Atlas Search index. Go to Atlas search tab > create new index > select collection > put the following text and create
```
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embedding": {
        "dimensions": 1536,
        "similarity": "cosine",
        "type": "knnVector"
      }
    }
  }
}
```
- Now You can start the app, and query your documents:
```
python3 extract_information.py
```

Go to your browser at [http://localhost:7860](http://localhost:7860) to see the results.

Resource: [freeCodeCamp](https://youtu.be/JEBDfGqrAUA?si=e8lDzjEnk0jn7ptQ)
