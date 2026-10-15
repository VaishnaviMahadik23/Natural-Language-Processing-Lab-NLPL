# Assignment 7: Sentiment Analysis using Machine Learning

## Overview
This project implements a **binary sentiment analysis system** to classify FMCG product reviews as positive or negative. It uses machine learning classifiers to evaluate sentiment and monitor brand health by detecting spikes in negative customer feedback.

## Features
- Text vectorization using TF-IDF
- Sentiment classification using Logistic Regression, Naive Bayes, and SVM
- Model evaluation using Accuracy, Confusion Matrix, and ROC-AUC
- Negative sentiment percentage calculation
- Brand health monitoring with alerts when negative sentiment exceeds 30%

## Technologies Used
- Python
- Scikit-learn
- CSV

## Dataset
The input dataset is stored in:

`data/fmcg_product_reviews.csv`

It contains customer reviews and sentiment labels (`0` for negative and `1` for positive).

## Installation

```bash
pip install scikit-learn
```

## How to Run

```bash
python Assignment7.py
```

## Output
The program displays model evaluation metrics and a brand monitoring status indicating normal conditions or a critical negative sentiment alert.

## Objective
To understand **machine learning-based sentiment classification, model evaluation, and customer feedback monitoring** for FMCG brand reputation management.
