import pandas as pd
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# File paths
faqs_path = Path(__file__).parent / "resources/faq_data.csv"

# Persistent Chroma client (creates ./chroma_db folder)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection_name_faq = "faqs"
groq_client = Groq()

# Encoder
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("Ingesting FAQ data into ChromaDB...")
        collection = chroma_client.create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )
        df = pd.read_csv(path)
        docs = df["question"].to_list()
        metadata = [{"answer": ans} for ans in df["answer"].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"FAQ Data successfully ingested into Chroma collection: {collection_name_faq}")
    else:
        print(f"Collection: {collection_name_faq} already exists")

def get_relevant_qa(query):
    collection = chroma_client.get_collection(name=collection_name_faq)
    result = collection.query(query_texts=[query], n_results=2)
    return result  

def faq_chain(query):
    result = get_relevant_qa(query)
    context = " ".join([r.get("answer", "") for r in result["metadatas"][0]])
    answer = generate_answer(query, context)
    return answer

def generate_answer(query, context):
    prompt = f"""
    Given the following context and question, generate an answer based on this context only.
    If the answer is not found in the context, kindly state "I don't know". 
    Do not try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {query}
    """

    chat_completion = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=os.environ["GROQ_MODEL"],
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    query = "Refund policy?"
    answer = faq_chain(query)
    print(answer)
