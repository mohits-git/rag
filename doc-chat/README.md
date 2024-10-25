# DocChat
Chat with your documentation

### Built with:
- Next.js
- Ollama
- MongoDB Atlas Vector Search
- LangChain and ai sdk

## Get Started 

### Install Ollama
Install Ollama for your platform from [here](https://ollama.com/)
- pull ollama embedding model
```
ollama pull mxbai-embed-large
```
- pull llama3.1 model
```
ollama pull llama3.1
```
> Ensure that ollama is running

### Project Setup
1. Clone the repository
2. Run `npm install`
3. Create a `.env.local` file in the root directory and add the following:
```
NODE_ENV=development
MONGODB_ATLAS_URI=<your_mongodb_atlas_uri>
```
4. Run `npm run embed` to create the embeddings for the documents
5. Create a vector index in MongoDB Atlas for the following:
```
dbName = "docs";
collectionName = "embeddings";
vectorIndexName = "vector_index";
keyName/path = 'embedding'
```
6. Run `npm run dev`
7. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
