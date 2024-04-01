# Named Entity Recognition (NER) with GLiNER

This repository contains code for performing Named Entity Recognition (NER) using the GLiNER model. NER is a sub-task of information extraction in Natural Language Processing (NLP) that classifies named entities into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, and more.

## Tools and Libraries Used

- **GLiNER**: GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoder (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.
- **Gradio**: Gradio is an easy-to-use library for creating web interfaces for machine learning models.

## Overview

The code demonstrates how to perform Named Entity Recognition (NER) using the GLiNER model. Here's a brief overview of the process:

1. **Model Loading**: The GLiNER model is loaded from the pretrained weights.
2. **Business Application**: The model is applied to a business-related text to identify entities such as company names, stock symbols, CEO names, etc.
3. **Court Documentation Application**: The model is applied to a legal document to identify entities such as case names, defendant names, plaintiff names, etc.
4. **Biomedical Application**: The model is applied to a biomedical text to identify entities such as patient age, gender, symptoms, diseases, etc.
5. **Highlighting App**: A web interface is created using Gradio to input text and visualize the named entities highlighted with labels.

## Example

The code provided in this repository illustrates how to implement the GLiNER model for various applications, including business, legal, and biomedical domains.

