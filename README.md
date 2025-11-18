# Sustainability Semantic Search Engine

A semantic search engine for exploring sustainability and corporate responsibility insights from 2024 public company reports(looking at 2023 data). COmpanies include Apple, Amazon, UnitedHealth Group, Chevron, Citi, NVIDIA, Tesla, Coca-Cola (will expand more comapnies in next iteration)

## Overview

This project uses AI powered text embeddings and a vector database to enable natural language search over sustainability and ESG related passages from company documents. Instead of simple keyword matching, the app retrieves results based on semantic similarity, which helps users to discover relevant insights even when they phrase queries differently from the original text. 
- All reports and content were collected by Hadil Ghazal 11/17/25 and are official publications from the companies listed
- No copyrighted text was used, summaries were paraphrased using (ChatGPT-5.1, 2025)'s assistance to avoid direct verbatim wording


## Tech Stack

- **Python**
- **SentenceTransformers** for text embeddings
- **ChromaDB** as the vector database
- **Streamlit** for the web app UI
- **Hugging Face Spaces** for deployment (later)

## Status

Currently setting up the project structure and dataset. Next steps include:
1. Building the embedding and vector store pipeline
2. Implementing a Streamlit UI for semantic search.
3. Deploying the app to Hugging Face Spaces
