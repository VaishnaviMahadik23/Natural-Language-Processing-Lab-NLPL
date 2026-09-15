
# Assignment 4: Word Embeddings & E-Commerce Recommendation

## Overview

This project demonstrates **word embeddings and semantic similarity** for an e-commerce dataset. It creates word vectors from product descriptions and uses them for analogy operations, dimensionality reduction, and product recommendations.

## Features

* Word vector generation using a custom embedding approach
* Word vector analogy using **A − B + C**
* **PCA** visualization of word embeddings in 2D
* Semantic similarity using **Cosine Similarity**
* E-commerce product recommendation based on query similarity
* JSON-based product dataset processing

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* PCA
* Cosine Similarity

## Dataset

The project uses product descriptions stored in:

`data/ecommerce_products.json`

## How to Run

Install the required libraries:

```bash
pip install numpy pandas scikit-learn
```

Run the program:

```bash
python Assignment4.py
```

## Output

The program displays:

* Word analogy results
* 2D PCA coordinates of selected words
* Product recommendations with similarity scores

## Objective

To understand **word embeddings, semantic relationships, vector operations, dimensionality reduction, and semantic product recommendation** using textual product data.
