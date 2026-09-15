# NLP Text Preprocessing Pipeline

## Overview

This project implements an **NLP text preprocessing pipeline** using **Python, NLTK, spaCy, and Pandas**. It demonstrates common techniques for cleaning and preparing text data for Natural Language Processing tasks.

## Features

* Text cleaning and normalization
* URL, mention, hashtag, emoji, and punctuation removal
* Tokenization using **Whitespace, NLTK, and spaCy**
* Stopword removal
* **Porter and Snowball stemming**
* **WordNet lemmatization**
* POS tagging using **NLTK and spaCy**
* Final corpus generation
* Cleaned dataset export to CSV
* Comparison of NLTK and spaCy preprocessing

## Technologies Used

* Python
* Pandas
* NLTK
* spaCy
* Regular Expressions (re)

## Dataset

The input dataset is read from:

`data/sample.csv`

The cleaned output is saved as:

`cleaned_data.csv`

## Installation

```bash
pip install pandas nltk spacy
python -m spacy download en_core_web_sm
```

Download the required NLTK resources before running the program:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

## How to Run

```bash
python Assignment1.py
```

The program displays the preprocessing results and generates the cleaned dataset.

## Objective

To understand and implement fundamental **NLP text preprocessing techniques** and compare text processing capabilities of **NLTK and spaCy**.

