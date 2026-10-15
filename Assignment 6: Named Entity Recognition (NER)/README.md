# Assignment 6: Named Entity Recognition (NER)

## Overview
This project implements **Named Entity Recognition (NER)** to extract clinical information from Electronic Health Record (EHR) discharge summaries using Python, Regular Expressions, and spaCy.

## Features
- Extracts drug names and dosages
- Identifies symptoms and diagnoses
- Rule-based clinical entity extraction
- Pretrained spaCy NER for general entity recognition
- Processes multiple patient discharge records from JSON

## Technologies Used
- Python
- spaCy
- Regular Expressions (`re`)
- JSON

## Dataset
The input dataset is stored in:

`data/clinical_discharge_summaries.json`

Each record contains a patient record ID and clinical text.

## Installation

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## How to Run

```bash
python main.py
```

## Output
The program displays extracted drugs, dosages, diagnoses, and symptoms for each patient record.

## Objective
To understand **Named Entity Recognition and rule-based information extraction** for identifying important clinical entities in medical text.
