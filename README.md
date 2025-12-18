# Football Data Chatbot ⚽

## Overview
This project focuses on building a data-aware chatbot that can answer natural language
questions using football data from the last 10 years.

The goal is to explore how structured sports data can be queried and summarized
using simple data processing pipelines and, later, large language models.

## Dataset
The data is sourced from Kaggle and contains historical football information across
multiple leagues and competitions.

Included datasets:
- `players.csv` – player metadata
- `clubs.csv` – club information
- `games.csv` – match-level data
- `appearances.csv` – player appearances per match
- `player_valuations.csv` – player market value history
- `competitions.csv` – competition metadata

> Note: Raw CSV files are not stored in this repository due to GitHub file size limits.
> They can be downloaded separately and placed inside the `data/` directory locally.

## Project Structure
football-data-chatbot/
├── data/ # Local CSV files (ignored by git)
├── README.md # Project documentation


## Current Status
The repository currently contains:
- Clean project structure
- Dataset identification and organization
- Documentation outlining project goals and scope

## Progress Log

### Day 1
- Identified and explored football datasets (10 years of data)
- Organized datasets locally
- Set up GitHub repository and documentation

### Planned Next Steps
- Load datasets using Python (pandas)
- Implement basic query functions (e.g. matches per club per season)
- Build a simple chatbot interface on top of the data layer
- Incrementally document progress in this repository

## Motivation
This project is part of a learning exercise to understand how data-driven systems
can be combined with natural language interfaces, particularly in the sports analytics domain.
