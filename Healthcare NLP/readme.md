# Healthcare NLP

This repository contains several Colab notebooks and scripts demonstrating various NLP techniques applied to healthcare data.

## Clinical Text Classification

This notebook focuses on classifying oncology reports into specific cancer types, including colon, thyroid, and lung cancer, using Spark NLP.

### Overview

#### Data Processing Pipeline

The project utilizes a Spark NLP pipeline to prepare text data from oncology reports for classification. The pipeline consists of the following stages:

- DocumentAssembler: Converts raw text into structured document objects.
- Tokenizer: Breaks down the documents into individual words or tokens.
- WordEmbeddings: Generates numerical representations (embeddings) for each token, capturing the semantic meaning of words specific to the healthcare domain.
- SentenceEmbeddings: Creates sentence-level embeddings by averaging the word embeddings within each sentence, capturing the overall meaning and context.

#### Classification Model

The project employs the ClassifierDL annotator from Spark NLP, which is a generic multi-class text classification model. It utilizes the state-of-the-art Universal Sentence Encoder as input and leverages a deep learning model (DNNs) built within TensorFlow. The model supports up to 100 classes, making it suitable for this multi-class classification task.

## Clinical Entity Resolution

Clinical entity resolution is essential for extracting valuable insights from clinical text data. This notebook demonstrates the process of linking recognized entities to corresponding medical terminologies, such as ICD-10 codes or RxNorm codes.

### Spark NLP for Healthcare

Spark NLP for Healthcare provides a comprehensive pipeline for clinical entity resolution. This pipeline leverages pre-trained models and incorporates the following steps:

- Named Entity Recognition (NER): This step extracts relevant clinical entities from the text, such as diseases, symptoms, and drugs.
- Sentence Embeddings: Sentence embeddings are generated for each entity using a pre-trained model like Sentence BERT (SBERT).
- Entity Resolution: These embeddings are then compared against a medical terminology database to identify the closest matching code.

#### Pipeline Overview

This pipeline utilizes several Spark NLP for Healthcare annotators to achieve accurate entity resolution with ICD-10 mapping:

- DocumentAssembler: Prepares the input text data for NLP processing.
- SentenceDetectorDL: Identifies individual sentences within the text.
- Tokenizer: Breaks down each sentence into individual tokens (words).
- WordEmbeddings: Generates word embeddings that capture the semantic meaning of each token.
- Clinical NER: Recognizes and extracts clinical entities (e.g., diagnoses, symptoms) from the text.
- NerConverterInternal: Filters and transforms extracted entities into chunks.
- Chunk2Doc: Converts the entity chunks back into document format for further processing.
- BertSentenceEmbeddings: Generates sentence embeddings for each entity chunk.
- SentenceEntityResolverModel: Utilizes a pre-trained model to find the closest ICD-10/LOINC/CPT code based on the sentence embeddings.

## Clinical Named Entity Recognition (NER)

Named Entity Recognition (NER) is a foundational element in Natural Language Processing (NLP) within the medical domain. This notebook demonstrates NER using the ZeroShotNerModel with the RoBERTa Question Answering model.

### Overview

#### Model Overview

- ZeroShotNerModel: Utilizes the RoBERTa Question Answering model for entity detection without relying on annotated datasets.
- The model is capable of extracting entities through crafted prompts, eliminating the need for manual labeling during training.

#### Pipeline Configuration

The project creates a pipeline for the Zero-Shot NER model, comprising the following stages:

1. DocumentAssembler: Prepares the clinical notes for further processing.
2. SentenceDetector: Identifies and separates sentences within the clinical notes.
3. Tokenizer: Breaks down sentences into individual tokens.
4. ZeroShotNer: Utilizes the ZeroShotNerModel to perform entity detection without embeddings models.
5. NerConverter: Converts the detected entities into a structured format for easy analysis.

To customize entity detection, a dictionary is created with specific questions for detecting entities and the corresponding labels desired in the results.

## Clinical Text Processing for Social Determinants of Health (SDOH)

This notebook utilizes Spark NLP to process clinical text, extract valuable information related to Social Determinants of Health (SDOH), and perform Named Entity Recognition (NER).

### Overview

The pipeline is designed to identify sentences, tokenize them, generate clinical word embeddings, and specifically recognize entities relevant to SDOH. The NER results are then converted into chunks for further analysis.

#### Features

- Clinical Text Processing: The pipeline processes clinical text data to uncover valuable insights related to SDOH.
- Named Entity Recognition (NER): Specialized NER models identify and categorize entities such as demographic information, socio-economic factors, and other determinants related to health.
- Word Embeddings: The project incorporates clinical word embeddings to capture the semantic relationships within the clinical text.
- Sentence Tokenization: Sentences within the clinical text are accurately identified and segmented for analysis.

