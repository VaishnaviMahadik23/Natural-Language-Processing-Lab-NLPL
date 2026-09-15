# Assignment 3: Bag-of-Words & TF-IDF Vectorization

## Overview

This project implements **Bag-of-Words (BoW)** and **TF-IDF** text vectorization using NumPy from scratch and verifies the results using scikit-learn. It also demonstrates document similarity for **academic plagiarism detection**.

## Features

* Bag-of-Words vocabulary and frequency matrix generation
* TF-IDF calculation using **Term Frequency (TF)** and **Inverse Document Frequency (IDF)**
* L2 normalization of TF-IDF vectors
* Verification using `CountVectorizer` and `TfidfVectorizer`
* Document similarity using **Cosine Similarity**
* Plagiarism detection using a configurable similarity threshold

## Technologies Used

* Python
* NumPy
* Scikit-learn
* JSON

## Dataset

The input dataset is stored in:

`data/academic_submissions.json`

Each record contains a document ID and its text content.

## How to Run

Install the required libraries:

```bash id="0lqv0e"
pip install numpy scikit-learn
```

Run the program:

```bash id="l8l4n7"
python Assignment3.py
```

## Output

The program displays:

* Vocabulary size
* TF-IDF matrix dimensions
* Comparison with scikit-learn
* Pairwise document cosine similarity
* **CLEAN** or **FLAGGED PLAGIARISM** status

## Objective

To understand **text vectorization, TF-IDF, cosine similarity, and document similarity analysis** and apply them to a basic academic plagiarism detection system.

