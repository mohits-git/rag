import { OllamaEmbeddings } from "@langchain/ollama";
import { MongoDBAtlasVectorSearch } from "@langchain/mongodb";
import mongoClientPromise from '@/app/lib/mongodb';
import { NextRequest, NextResponse } from "next/server";

export const runtime = 'nodejs';

export async function POST(req: NextRequest) {
  const client = await mongoClientPromise;
  const dbName = "docs";
  const collectionName = "embeddings";
  const collection = client.db(dbName).collection(collectionName);

  const question = await req.text();
  console.debug("Question: ", question)

  const embeddings = new OllamaEmbeddings({
    model: "mxbai-embed-large",
    baseUrl: "http://localhost:11434",
  });

  console.debug("Embeddings Created")
  const vectorStore = new MongoDBAtlasVectorSearch(
    embeddings, {
    collection,
    indexName: "vector_index",
    textKey: "text",
    embeddingKey: "embedding",
  });

  console.debug("Vector Store Created")
  const retriever = vectorStore.asRetriever({
    searchType: "mmr",
    searchKwargs: {
      fetchK: 20,
      lambda: 0.1,
    },
  });

  console.debug("Retriever Created")
  const retrieverOutput = await retriever.invoke(question);

  console.debug("RETRIEVER OUTPUT: ", retrieverOutput);
  return NextResponse.json(retrieverOutput);
}
