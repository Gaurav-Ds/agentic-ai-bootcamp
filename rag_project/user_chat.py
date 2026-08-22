from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

brain=OpenAI()

embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large"
    
)

vector_store=QdrantVectorStore.from_existing_collection(
    collection_name="rag_collection",
    embedding=embedding_model,
    url="http://localhost:6333"

)

user_input=input(">> ")


search_results=vector_store.similarity_search(user_input)

context="\n\n\n".join([f'page_content: {result.page_content}\n page_number: {result.metadata["page_label"]}\n file_location: {result.metadata["source"]}' for result in search_results])


SYSTEM_PROMPT=f"""You are a helpful assistant that answers questions based on the context provided. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context} """

chat_response=brain.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]   )


print(context)

print("llm response: ",chat_response.choices[0].message.content)
                    