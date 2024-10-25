import { StreamingTextResponse, Message } from 'ai';
import { ChatOllama } from '@langchain/ollama';
import { AIMessage, HumanMessage } from '@langchain/core/messages';
import { NextResponse } from 'next/server';

export const runtime = 'nodejs';

export async function POST(req: Request) {
  try {
    const { messages } = await req.json();
    const currentMessageContent = messages[messages.length - 1].content;
    console.debug("Message: ", currentMessageContent);

    const vectorSearch = await fetch("http://localhost:3000/api/vectorSearch", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: currentMessageContent,
    }).then((res) => res.json());
    console.debug("Vector Search: ", vectorSearch);

    const TEMPLATE = `You are a very enthusiastic freeCodeCamp.org representative who loves to help people! Given the following sections from the freeCodeCamp.org contributor documentation, answer the question using only that information, outputted in markdown format. If you are unsure and the answer is not explicitly written in the documentation, say "Sorry, I don't know how to help with that."
    
    Context sections:
    ${JSON.stringify(vectorSearch)}
    Question: """
    ${currentMessageContent}
    """
    `;
    messages[messages.length - 1].content = TEMPLATE;

    const llm = new ChatOllama({
      model: "llama3.1",
      baseUrl: "http://localhost:11434",
      streaming: true,
      maxRetries: 2,
    });

    const stream = await llm.stream(
      (messages as Message[]).map(m =>
        m.role == 'user'
          ? new HumanMessage(m.content)
          : new AIMessage(m.content),
      ),
      {},
    );

    if (!stream) {
      return NextResponse.json({ error: "Failed to create stream" }, { status: 500 });
    }

    // Convert LangChain stream to ReadableStream of UTF-8 encoded bytes
    const textStream = new ReadableStream({
      async start(controller) {
        try {
          for await (const chunk of stream) {
            const text = chunk.content.toString();
            if (text) {
              // Encode the text as UTF-8
              const encoder = new TextEncoder();
              const encoded = encoder.encode(text);
              controller.enqueue(encoded);
            }
          }
          controller.close();
        } catch (error) {
          controller.error(error);
        }
      },
    });

    return new StreamingTextResponse(textStream);
  } catch (error) {
    console.error("Error in chat endpoint:", error);
    return NextResponse.json({ error: "Internal server error" }, { status: 500 });
  }
}
