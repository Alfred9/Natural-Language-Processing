# Medical Named Entity Recognition App

A Streamlit application for extracting medical entities from clinical text using Stanza with the MIMIC/i2b2 model.

![Medical NER App Screenshot](https://raw.githubusercontent.com/yourusername/medical-ner-app/main/screenshot.png)

## Features

- Extract medical entities from clinical text
- Support for text input, PDF, Word documents, and TXT files
- Entity visualization and statistics
- Based on Stanza's MIMIC pipeline with i2b2 NER model
- Recognizes medical problems, treatments, and tests

## Live Demo

Try it out on Streamlit Cloud: [Medical NER App](https://medical-ner-app.streamlit.app/)

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/medical-ner-app.git
cd medical-ner-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default web browser. You can:

1. Enter medical text directly in the text area
2. Upload a PDF, Word document, or TXT file
3. Click "Extract Entities" to process the text
4. View the extracted entities and statistics

## Deployment on Streamlit Cloud

To deploy this app on Streamlit Cloud:

1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select the repository
4. Configure app settings and deploy

## Model Information

The app uses Stanza's MIMIC pipeline with the i2b2 NER model, which is specifically designed for biomedical and clinical text processing. It recognizes:

- **PROBLEM**: Medical problems/conditions
- **TREATMENT**: Treatments, medications, procedures
- **TEST**: Diagnostic tests and measures

## Example Text

Here's a sample text you can use to test the app:

```
The patient was a 56-year-old female admitted on 5/12/2021 with chief complaint of chest pain. History of diabetes mellitus, hypertension, and COPD. ECG showed normal sinus rhythm. Labs revealed elevated troponin at 0.12. Patient was treated with aspirin 325mg, Plavix 75mg, and IV heparin. Echo showed preserved EF of 60% with mild MR.
```

## License

MIT License

## Acknowledgements

- [Stanza](https://stanfordnlp.github.io/stanza/) for the clinical NLP library
- [Streamlit](https://streamlit.io/) for the web application framework
- [i2b2](https://www.i2b2.org/) for the named entity recognition training data
