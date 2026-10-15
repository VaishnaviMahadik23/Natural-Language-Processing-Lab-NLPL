
# Assignment 10: Prompt Engineering Techniques for LLMs

## Overview
This project demonstrates prompt engineering techniques for legal contract analysis. It generates Zero-Shot, Few-Shot, and Chain-of-Thought (CoT) prompt templates to support contract summarization, risk clause identification, and plain-language brief generation.

## Features
- Zero-Shot prompt generation
- Few-Shot prompting with example input-output pairs
- Chain-of-Thought prompt template for structured analysis
- Legal contract summarization and risk clause detection prompts
- Identification of obligations, key dates, and liability limitations
- Comparison of different prompt strategies

## Technologies Used
- Python
- JSON
- Prompt Engineering
- Large Language Models (LLMs)

## Dataset
`data/sample_contracts.json`

The dataset contains sample legal contracts, with contract text stored in the `text` field.

## Installation
No external libraries are required.

## How to Run
```bash
python Assignment10.py
```

## Output
Displays a sample contract and the generated Zero-Shot, Few-Shot, and Chain-of-Thought prompt templates.

## Objective
Understand how prompt design influences LLM-based legal document analysis and supports contract summarization, risk identification, and plain-language explanations.

**Note:** The current script generates and displays prompts; it does not call an LLM or evaluate actual output quality. The One-Shot strategy is mentioned in the assignment description but is not implemented in the provided code.
