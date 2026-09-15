# Assignment 3: Regular Expressions & Text Cleaning

Resume Information Extraction using Regular Expressions

## Overview

This project extracts structured information from resume text using **Python, Regular Expressions (Regex), and Pandas**. A custom `TextCleaner` class is used to identify and extract important resume details.

## Features

* Extracts **Name, Email, Phone Number, and Experience**
* Identifies common **technical skills**
* Extracts URLs and hashtags
* Removes HTML and JSON tags
* Converts unstructured resume text into structured data
* Exports the extracted information to a CSV file

## Technologies Used

* Python
* Pandas
* Regular Expressions (`re`)

## Dataset

The input dataset is:

`data/resumes.csv`

The extracted output is saved as:

`extracted_resume_data.csv`

## Installation

```bash
pip install pandas
```

## How to Run

```bash
python Assignment2.py
```

The program reads the resume dataset, extracts the required information, displays the results, and saves the structured data to a CSV file.

## Objective

To understand **text extraction, pattern matching, and data cleaning** techniques for converting unstructured resume data into structured information.
