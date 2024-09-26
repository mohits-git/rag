from pymongo import MongoClient
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import config

client = MongoClient(config.DATABASE_URL)
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

embeddings = OpenAIEmbeddings(openai_api_key=config.OPENAI_API_KEY)

vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)


def query_data(query):
    docs = vectorStore.similarity_search(query, K=1)
    as_output = docs[0].page_content

    llm = OpenAI(openai_api_key=config.OPENAI_API_KEY, temperature=0)
    retriever = vectorStore.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm, chain_type="stuff", retriever=retriever)
    retriever_output = qa.run(query)

    return as_output, retriever_output
