# Football Data Chatbot

## Overview
This project focuses on building a data-aware chatbot that can answer natural language questions using football data from the last 10 years. The primary goal is to understand how large language models (LLMs) can be connected to real, structured sports data and what kind of data preparation is required for them to produce meaningful and grounded responses.

At this stage, the focus is on setting up a basic framework for building such a chatbot and exploring how structured football datasets can be made usable for LLM-based querying.

---

## Dataset
The data is sourced from Kaggle and contains historical football information across multiple leagues and competitions.

Included datasets:
- `players.csv` – player metadata  
- `clubs.csv` – club information  
- `games.csv` – match-level data  
- `appearances.csv` – player appearances per match  
- `player_valuations.csv` – player market value history  
- `competitions.csv` – competition metadata  

These datasets are relational and fairly large, which makes them realistic but also challenging to work with in the context of LLMs.

**Note:** Raw CSV files are not stored in this repository due to GitHub file size limits. They can be downloaded separately and placed inside the `data/` directory locally.

---

## What I’m Learning

### Working with structured data and LLMs
One of the first things I am learning through this project is that LLMs cannot directly reason over large CSV files in a reliable way. While they can understand small tabular examples, they are not designed to ingest or operate over thousands of structured rows, joins, or filters.

This means that some form of data transformation is required before the data can be used effectively in a chatbot setting.

---

### Converting structured rows into football facts
To address this, I am exploring the idea of converting structured rows into short, human-readable football facts. Instead of passing raw tables to the model, each row (or small group of rows) is transformed into a sentence or short paragraph describing something meaningful, such as a player appearance, a match result, or a club’s participation in a competition.

This approach makes the data:
- Easier for language models to understand
- Suitable for semantic search using embeddings
- More flexible for natural language queries

This conversion process is an important part of the project and is being developed iteratively.

---

## Planned Approach
The chatbot will be built using a retrieval-based framework:

1. Football datasets are loaded and filtered to the last 10 years.
2. Structured rows are converted into short, readable football facts.
3. These facts are embedded and stored in a vector database.
4. User queries retrieve the most relevant facts.
5. A language model generates answers based only on the retrieved data.

The initial implementation will focus on correctness and clarity rather than completeness.

---

## Project Structure
football-data-chatbot/
├── data/ # Local CSV files (ignored by git)
├── app/ # Data ingestion and chatbot logic (in progress)
├── docs/ # Development notes and progress logs
├── README.md # Project documentation


---

## Current Status
- Football datasets identified and explored
- Project structure and basic framework set up
- Initial understanding developed around how to adapt structured data for LLM-based querying

---

## Progress Log

### Day 1
- Explored the structure and scale of football datasets from the last 10 years
- Identified challenges with using large CSV files directly with LLMs
- Set up the repository structure and documentation
- Defined a basic framework for building a retrieval-based football chatbot

---

## Next Steps
- Load and preprocess selected datasets using Python
- Implement the conversion of structured rows into textual football facts
- Build a small-scale retrieval-based prototype using embeddings
- Extend coverage to additional datasets once the core pipeline is working


