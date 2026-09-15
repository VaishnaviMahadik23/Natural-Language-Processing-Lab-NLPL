# ==========================================================
# NLP Text Preprocessing Pipeline using NLTK and spaCy
# ==========================================================

import re
import pandas as pd
import nltk
import spacy

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# ----------------------------------------------------------
# Load spaCy Model
# ----------------------------------------------------------

nlp = spacy.load("en_core_web_sm")

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("data/sample.csv")

print("\n==============================")
print("Original Dataset")
print("==============================")
print(df)

# ----------------------------------------------------------
# Initialize NLP Tools
# ----------------------------------------------------------

stop_words = set(stopwords.words("english"))

porter = PorterStemmer()

snowball = SnowballStemmer("english")

lemmatizer = WordNetLemmatizer()

# ----------------------------------------------------------
# Function to Clean Text
# ----------------------------------------------------------

def clean_text(text):

    # Convert to string
    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove Twitter Mentions
    text = re.sub(r"@\w+", "", text)

    # Remove Hashtags Symbol
    text = re.sub(r"#", "", text)

    # Remove Emojis
    text = re.sub(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "]+",
        "",
        text,
    )

    # Remove Punctuation
    text = re.sub(r"[^\w\s]", "", text)

    return text

# ----------------------------------------------------------
# Apply Cleaning
# ----------------------------------------------------------

df["Clean_Text"] = df["text"].apply(clean_text)

# ----------------------------------------------------------
# Tokenization
# ----------------------------------------------------------

print("\n==============================")
print("TOKENIZATION")
print("==============================")

for sentence in df["Clean_Text"]:

    print("\nSentence:")
    print(sentence)

    print("\nWhitespace Tokenizer")
    print(sentence.split())

    print("\nNLTK Tokenizer")
    print(word_tokenize(sentence))

    print("\nspaCy Tokenizer")
    doc = nlp(sentence)
    print([token.text for token in doc])

# ----------------------------------------------------------
# Stopword Removal
# ----------------------------------------------------------

def remove_stopwords(sentence):

    words = word_tokenize(sentence)

    filtered = []

    for word in words:

        if word not in stop_words:

            filtered.append(word)

    return filtered

df["Stopword_Removal"] = df["Clean_Text"].apply(remove_stopwords)

# ----------------------------------------------------------
# Porter Stemming
# ----------------------------------------------------------

def porter_stem(words):

    return [porter.stem(word) for word in words]

df["Porter_Stem"] = df["Stopword_Removal"].apply(porter_stem)

# ----------------------------------------------------------
# Snowball Stemming
# ----------------------------------------------------------

def snowball_stem(words):

    return [snowball.stem(word) for word in words]

df["Snowball_Stem"] = df["Stopword_Removal"].apply(snowball_stem)

# ----------------------------------------------------------
# Lemmatization
# ----------------------------------------------------------

def lemmatize(words):

    return [lemmatizer.lemmatize(word) for word in words]

df["Lemmatization"] = df["Stopword_Removal"].apply(lemmatize)

# ----------------------------------------------------------
# POS Tagging using NLTK
# ----------------------------------------------------------

def nltk_pos(words):

    return pos_tag(words)

df["NLTK_POS"] = df["Lemmatization"].apply(nltk_pos)

# ----------------------------------------------------------
# POS Tagging using spaCy
# ----------------------------------------------------------

def spacy_pos(sentence):

    doc = nlp(sentence)

    return [(token.text, token.pos_) for token in doc]

df["spaCy_POS"] = df["Clean_Text"].apply(spacy_pos)

# ----------------------------------------------------------
# Final Clean Corpus
# ----------------------------------------------------------

df["Final_Corpus"] = df["Lemmatization"].apply(lambda x: " ".join(x))

# ----------------------------------------------------------
# Display Results
# ----------------------------------------------------------

print("\n==============================")
print("FINAL OUTPUT")
print("==============================")

columns = [
    "text",
    "Clean_Text",
    "Stopword_Removal",
    "Porter_Stem",
    "Snowball_Stem",
    "Lemmatization",
    "Final_Corpus",
]

print(df[columns])

# ----------------------------------------------------------
# Save Clean Dataset
# ----------------------------------------------------------

df.to_csv("cleaned_data.csv", index=False)

print("\n=========================================")
print("Cleaned dataset saved as cleaned_data.csv")
print("=========================================")

# ----------------------------------------------------------
# NLTK vs spaCy Comparison
# ----------------------------------------------------------

print("\n==============================")
print("NLTK vs spaCy Comparison")
print("==============================")

sample = df["Clean_Text"][0]

print("\nSample Sentence")
print(sample)

print("\nNLTK Tokens")
print(word_tokenize(sample))

print("\nspaCy Tokens")
doc = nlp(sample)
print([token.text for token in doc])

print("\nNLTK POS")
print(pos_tag(word_tokenize(sample)))

print("\nspaCy POS")
print([(token.text, token.pos_) for token in doc])