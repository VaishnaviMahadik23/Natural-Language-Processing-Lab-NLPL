# Assignment 8: Transformer-Based Multilingual Sentiment Analysis

## Overview
This project implements multilingual sentiment analysis using Hugging Face Transformers to analyze social media posts in English, Hindi, and Marathi. It predicts sentiment labels and confidence scores, with a fallback heuristic when the transformer pipeline is unavailable.

## Features
- Multilingual social media text analysis
- Sentiment prediction using Hugging Face Transformers
- Sentiment labels with confidence scores
- Fallback rule-based sentiment classification
- Dashboard-style output displaying language, text, sentiment, and confidence

## Technologies Used
- Python
- Hugging Face Transformers
- DistilBERT
- CSV

## Dataset
`data/multilingual_opinion_tweets.csv`

The dataset contains social media posts with `text` and `lang` columns.

## Installation
```bash
pip install transformers torch
```

## How to Run
```bash
python Assignment8.py
```

## Output
Displays each social media post's language, predicted sentiment, and confidence score.

## Objective
Understand transformer-based sentiment analysis and multilingual opinion mining for analyzing social media feedback in English, Hindi, and Marathi.
