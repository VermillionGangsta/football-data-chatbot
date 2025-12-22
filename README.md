# Football Data Chatbot

## Overview
This project explores how to build a data-aware chatbot over real-world football data from the last 10 years. The focus so far has been on understanding how large language models (LLMs) interact with structured data and what kind of data preparation and system design is required before a chatbot can answer questions reliably.

Rather than starting directly with a UI or answer generation, the project prioritizes building a clean data ingestion and retrieval pipeline that can later be extended into a full chatbot.

---

## Dataset
The data is sourced from Kaggle and consists of multiple structured CSV files covering different aspects of football data:

- `players.csv` – player metadata (name, position, nationality, date of birth)
- `games.csv` – match-level information (teams, date, competition, score)
- `clubs.csv` – club metadata
- `appearances.csv` – player appearances per match
- `player_valuations.csv` – historical player market values
- `competitions.csv` – competition and league metadata

These datasets are relational and fairly large, which makes them realistic but also challenging to work with directly using LLMs.

**Note:** Raw CSV files are not included in the repository due to size constraints and are expected to be placed locally in the `data/` directory.

---

## Key Learnings So Far

### Working with structured data and LLMs
One of the first insights from this project is that LLMs cannot directly reason over large CSV files in a reliable way. While they can understand small tabular examples, they are not designed to ingest thousands of structured rows, perform joins, or handle large-scale filtering.

This makes it necessary to transform structured data into a format that is more compatible with language models.

---

### Converting rows into human-readable football facts
To bridge this gap, the project converts structured rows into short, human-readable football facts. For example:
- A player row becomes a sentence describing the player’s position, nationality, and birth date
- A match row becomes a sentence describing the teams, competition, date, and final score

This representation makes the data:
- Easier for embeddings to capture semantic meaning
- Searchable using vector similarity
- Suitable for retrieval-based question answering

This transformation step is a core part of the project.

---

## Current Architecture
The system currently follows a retrieval-first design:

1. Load structured football datasets (players, games)
2. Convert rows into textual football facts
3. Store these facts locally
4. Generate embeddings for the facts using a local embedding model
5. Index embeddings using a FAISS vector store
6. Retrieve relevant facts for a given natural language query

Answer generation and UI layers are intentionally deferred until the retrieval pipeline is solid.

---
## Project Structure
football-data-chatbot/
├── data/ # Local CSV files and generated artifacts (ignored by git)
├── app/
│ ├── ingest.py # CSV → football facts
│ ├── vector_store.py # Embedding + FAISS index creation
├── README.md


---

## Current Status
- Explored and understood multi-table football datasets
- Built an ingestion pipeline for players and games data
- Converted structured rows into human-readable football facts
- Created a local embedding-based vector store using FAISS
- Validated semantic retrieval over football data

---

## Next Steps
- I have to make a streamlit UI for interaction where I can interact with different queries



