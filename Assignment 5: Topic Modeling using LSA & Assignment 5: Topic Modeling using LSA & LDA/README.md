# Assignment 5: Topic Modeling using LSA and LDA

## Overview
This project applies **Latent Semantic Analysis (LSA)** and **Latent Dirichlet Allocation (LDA)** to discover hidden topics in telecom customer support tickets. It extracts important keywords to identify common customer issues and support operational decision-making.

## Features
- Topic modeling using LSA and LDA
- Automatic topic keyword extraction
- Text vectorization using TF-IDF and CountVectorizer
- Identification of patterns in telecom support tickets
- Comparison of LSA and LDA topic results

## Technologies Used
- Python
- Scikit-learn
- CSV

## Dataset
The input dataset is stored in:

`data/telecom_support_tickets.csv`

The dataset contains customer support ticket descriptions in a `text` column.

## Installation

```bash
pip install scikit-learn
```

## How to Run

```bash
python main.py
```

## Output
The program displays the top keywords for three topics identified by LDA and LSA.

## Objective
To understand **unsupervised topic modeling** and apply it to telecom support ticket analysis for identifying recurring customer issues and improving operational decisions.
