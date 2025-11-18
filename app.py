# Streamlit semantic search app for sustainability report insights
#No AI was used to generate this code, authored by HG 11/18/25

#initial imports
#v2 import adding os and pandas for huggingface readability, failed last push
import os
import pandas as pd
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer

#Loading Chroma
client = chromadb.PersistentClient(path="vector_store")
collection = client.get_or_create_collection(
    name="sustainability_sections",
    metadata={"hnsw:space": "cosine"}
)

#Loading embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


#need conditional logic for huggingface. So if the setup is empty, it is built from the csv directly

if collection.count() == 0:
    csv_path = os.path.join("data", "sustainability_sections.csv")
    df = pd.read_csv(csv_path)

    documents = df["text"].tolist()
    metadatas = df[["company", "year", "section_title"]].to_dict(orient="records")
    ids = [f"doc_{i}" for i in range(len(df))]

    embeddings = model.encode(documents).tolist()

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )


#Streamlit UI
st.title("Sustainability Semantic Search Engine")
st.write("Search across sustainability, ESG, and environmental commitments from major companies.")

query = st.text_input("Enter your search query:")
st.caption("Example searches: *'renewable energy'*, *'carbon reduction'*, *'water stewardship'*, *'zero waste'*")


if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        #Embedding user query
        query_embedding = model.encode(query).tolist()

        #Query Chroma
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )

        st.subheader("Top Results")

        for i in range(len(results["documents"][0])):
            st.markdown("---")
            st.write(f"**Company:** {results['metadatas'][0][i]['company']}")
            st.write(f"**Year:** {results['metadatas'][0][i]['year']}")
            st.write(f"**Section:** {results['metadatas'][0][i]['section_title']}")
            st.write(f"**Text:** {results['documents'][0][i]}")