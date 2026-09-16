# Assignment 3: Bag-of-Words & TF-IDF Vectorization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from collections import Counter
import math

corpus = [
    'Machine learning is a subset of artificial intelligence',
    'Deep learning uses neural networks for pattern recognition',
    'Natural language processing handles text and speech data',
    'NLP techniques include tokenization and named entity recognition',
    'Artificial intelligence is transforming healthcare and finance',
    'Neural networks are inspired by the human brain structure'
]
labels = ['ML', 'DL', 'NLP', 'NLP', 'AI', 'DL']

# BoW from scratch
all_words = [w for doc in corpus for w in doc.lower().split()]
vocabulary = sorted(set(all_words))
bow_matrix = [[Counter(d.lower().split()).get(w,0) for w in vocabulary] for d in corpus]
print('BoW Matrix shape:', len(bow_matrix), 'x', len(vocabulary))

# TF-IDF from scratch
N = len(corpus)
tf_matrix = [[Counter(d.lower().split()).get(w,0)/len(d.split()) for w in vocabulary] for
d in corpus]
idf_vector = [math.log(N/sum(1 for d in corpus if w in d.lower().split()))+1 for w in
vocabulary]
tfidf_scratch = np.array(tf_matrix) * np.array(idf_vector)

# Sklearn verification
cv = CountVectorizer()
bow_sklearn = cv.fit_transform(corpus).toarray()
tv = TfidfVectorizer()
tfidf_sklearn = tv.fit_transform(corpus).toarray()
print('Sklearn BoW shape:', bow_sklearn.shape)
print('Sklearn TF-IDF shape:', tfidf_sklearn.shape)

# Top-5 keywords per class
feature_names = tv.get_feature_names_out()
for label in sorted(set(labels)):
    indices = [i for i,l in enumerate(labels) if l==label]
    mean_tfidf = tfidf_sklearn[indices].mean(axis=0)
    top_idx = mean_tfidf.argsort()[-5:][::-1]
    print(f'{label}: {[feature_names[i] for i in top_idx]}')