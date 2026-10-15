# Assignment 9: Text Classification Using Deep Learning (LSTM / BERT)

## Overview
This project demonstrates multi-class news article classification and category routing using simulated benchmarks for a Bi-directional LSTM (PyTorch) and DistilBERT (Transformers). It compares model accuracy and inference latency for routing news into World, Sports, Business, and Sci/Tech categories.

## Features
- Multi-class news category classification
- Bi-directional LSTM and DistilBERT benchmark comparison
- Inference latency measurement
- Validation against the target latency of less than 200 ms
- Automatic routing of articles to the appropriate category desk

## Technologies Used
- Python
- PyTorch (LSTM concept)
- Hugging Face Transformers (DistilBERT concept)
- CSV

## Dataset
`data/news_articles.csv`

The dataset contains news article titles (`title`) and category labels (`category`).

## Installation
No external libraries are required for the current simulation script.

## How to Run
```bash
python Assignment9.py
```

## Output
Displays simulated model accuracy, inference latency, target status, and news article category routing.

## Objective
Understand deep learning-based text classification and compare LSTM and transformer approaches for news categorization. **Note:** The current script simulates benchmark results; it does not train or run actual LSTM or DistilBERT models.
