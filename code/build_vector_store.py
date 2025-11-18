#No AI was used to generate this code. Authored by HG 11/18/25
# V2 Updated to use chromadb.PersistentClient because the old API raised a ValueError and didnt work
# initial imports
import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd
import os

#loading dataset
def build_vector_store():
    csv_path = os.path.join("data", "sustainability_sections.csv")
    df = pd.read_csv(csv_path)

    #Chroma
    client = chromadb.PersistentClient(path="vector_store")

    collection = client.get_or_create_collection(
        name="sustainability_sections",
        metadata={"hnsw:space": "cosine"}
    )

    #Loading the embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    #Preparing documents and metadata
    documents = df["text"].tolist()
    metadatas = df[["company", "year", "section_title"]].to_dict(orient="records")
    ids = [f"doc_{i}" for i in range(len(df))]

    #Generating the embeddings
    embeddings = model.encode(documents).tolist()

    #Adding to Chroma
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    #confirmation
    print("Vector store built and saved to: vector_store/")

if __name__ == "__main__":
    build_vector_store()
