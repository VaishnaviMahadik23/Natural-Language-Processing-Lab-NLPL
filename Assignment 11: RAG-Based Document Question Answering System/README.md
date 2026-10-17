# Assignment 11: RAG-Based Document Question Answering System

## Overview
This project implements a Retrieval-Augmented Generation (RAG)-based question-answering system that retrieves relevant information from a university handbook to answer student queries about examinations, admissions, and hostel rules. It uses TF-IDF vectorization and cosine similarity for context retrieval.

## Features
- University handbook document chunking and indexing
- TF-IDF-based text vectorization
- Top-1 context retrieval using cosine similarity
- Context-based answer extraction
- Retrieval confidence score calculation
- Automated responses to common student queries

## Technologies Used
- Python
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Dataset
`data/university_handbook.txt`

The dataset contains university handbook sections covering examinations, admissions, hostel regulations, and student policies.

## Installation
```bash
pip install scikit-learn
```

## How to Run
```bash
python Assignment11.py
```

## Output
Displays the number of indexed handbook chunks, student queries, retrieved answers, and confidence scores.

## Objective
Understand document chunking, vector-based retrieval, and context-grounded question answering for university student-support systems.

**Note:** The current implementation uses TF-IDF and cosine similarity rather than FAISS or a transformer-based embedding model. It extracts an answer from the retrieved text instead of generating one with an LLM. ROUGE and BLEU evaluation metrics are not implemented in the provided code.
