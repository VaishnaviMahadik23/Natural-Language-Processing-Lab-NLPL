# Natural Language Processing Lab (NLPL)

A collection of **11 Python-based Natural Language Processing (NLP) assignments** exploring text processing, machine learning, deep learning, transformer models, prompt engineering, and Retrieval-Augmented Generation (RAG).

**Repository:** [Natural-Language-Processing-Lab-NLPL](https://github.com/VaishnaviMahadik23/Natural-Language-Processing-Lab-NLPL)

## Overview

This repository contains practical implementations of fundamental and advanced NLP concepts. Each assignment focuses on a specific technique, with applications such as resume information extraction, sentiment analysis, news classification, legal document analysis, and university handbook question answering.

The repository is intended for students and learners who want hands-on experience with Python NLP libraries, machine learning algorithms, and modern language model techniques.

## Assignments

| No. | Assignment | Key Concepts |
|---|---|---|
| 1 | Text Preprocessing Pipeline | Tokenization, stopword removal, stemming, lemmatization, POS tagging |
| 2 | Resume Information Extraction | Regular expressions, email and phone extraction, skill and URL detection |
| 3 | Bag-of-Words and TF-IDF | Text vectorization, feature extraction, cosine similarity |
| 4 | Word Embeddings and E-Commerce Recommendation | Word vectors, word analogies, PCA, similarity-based recommendations |
| 5 | Topic Modeling | Latent Dirichlet Allocation (LDA), Latent Semantic Analysis (LSA) |
| 6 | Named Entity Recognition (NER) | Entity extraction, rule-based patterns, spaCy |
| 7 | Sentiment Analysis Using Machine Learning | TF-IDF, Logistic Regression, Naive Bayes, SVM, model evaluation |
| 8 | Transformer-Based Sentiment Analysis | Hugging Face Transformers, multilingual sentiment analysis |
| 9 | Deep Learning Text Classification | Bi-directional LSTM, DistilBERT concepts, news category routing |
| 10 | Prompt Engineering for LLMs | Zero-Shot, Few-Shot, Chain-of-Thought prompting, legal contract analysis |
| 11 | RAG-Based Document Question Answering | Document chunking, TF-IDF retrieval, cosine similarity, context-based answers |

## Technologies Used

- **Programming Language:** Python
- **NLP Libraries:** NLTK, spaCy
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy, CSV, JSON
- **Deep Learning:** PyTorch concepts, LSTM
- **Transformers:** Hugging Face Transformers, DistilBERT
- **NLP Techniques:** TF-IDF, word embeddings, NER, topic modeling, sentiment analysis
- **LLM Concepts:** Prompt engineering and Retrieval-Augmented Generation (RAG)

## Repository Structure

```text
Natural-Language-Processing-Lab-NLPL/
├── Assignment-01/
├── Assignment-02/
├── Assignment-03/
├── Assignment-04/
├── Assignment-05/
├── Assignment-06/
├── Assignment-07/
├── Assignment-08/
├── Assignment-09/
├── Assignment-10/
├── Assignment-11/
└── README.md
```

*The structure above is illustrative. Folder names may differ from the actual repository.*

## Getting Started

### Prerequisites

- Python 3.9 or later recommended
- pip package manager
- Git
- A code editor such as VS Code or PyCharm

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/VaishnaviMahadik23/Natural-Language-Processing-Lab-NLPL.git
```

**2. Navigate to the repository**

```bash
cd Natural-Language-Processing-Lab-NLPL
```

**3. Create a virtual environment (recommended)**

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

**4. Install the required libraries**

Install the dependencies needed by the assignment you want to run:

```bash
pip install numpy pandas scikit-learn nltk spacy
```

For Assignment 8, install the additional transformer dependencies:

```bash
pip install transformers torch
```

Some assignments may also require NLTK resources, a spaCy language model, or the relevant dataset files. Follow the instructions in each assignment's source code.

## Running the Assignments

1. Open the folder containing the assignment.
2. Check that its required dataset is present in the expected location.
3. Install any assignment-specific dependencies.
4. Run the corresponding Python script.

Example:

```bash
python main.py
```

Use the actual Python filename provided in the selected assignment folder.

## Learning Outcomes

By completing these assignments, learners can:

- Apply text cleaning and linguistic preprocessing techniques.
- Extract structured information from unstructured text.
- Convert text into numerical representations using BoW and TF-IDF.
- Explore word embeddings and semantic similarity.
- Discover topics and identify named entities in documents.
- Build and evaluate machine learning-based sentiment classifiers.
- Understand multilingual transformer-based NLP.
- Explore deep learning approaches to text classification.
- Design prompts for language-model-based document analysis.
- Implement basic document retrieval and question-answering pipelines.

## Important Notes

- Some assignments demonstrate concepts through simulations or rule-based fallbacks rather than fully trained models.
- Assignment 9 uses simulated benchmark results rather than training actual LSTM and DistilBERT models.
- Assignment 10 generates prompt templates but does not call an LLM to analyze contracts.
- Assignment 11 implements TF-IDF-based retrieval and answer extraction; it does not include an LLM-based answer generator or ROUGE/BLEU evaluation.
- Results depend on the input datasets, installed dependencies, and implementation used.

## Purpose

The goal of this repository is to provide a practical learning resource for understanding NLP concepts, experimenting with language-processing techniques, and building a foundation for more advanced AI and language-model applications.

## Author

**Vaishnavi Mahadik**

GitHub: [@VaishnaviMahadik23](https://github.com/VaishnaviMahadik23)

## License

This repository is intended for educational and academic purposes. Add a license file if you wish to specify the terms under which others may use, modify, or distribute the code.
