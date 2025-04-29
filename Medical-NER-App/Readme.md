# 🧬 Biomedical NER with Azure OpenAI / OpenAI API

This is a simple Python app that extracts biomedical entities (e.g., diseases, drugs, symptoms, treatments) from clinical notes using large language models.

You can run it using:
- **Azure OpenAI Service** (recommended for enterprise or cloud deployment), or
- **OpenAI API** (via direct API key from OpenAI)

---

## 🔧 Features

- Extracts structured entities in JSON format from clinical text
- Built-in support for `gpt-4o`, `gpt-4`, or your own Azure OpenAI deployment
- Uses structured prompts to improve model consistency
- Includes logging and error handling
- Easy to run locally via CLI

---

## 📦 Requirements

- Python 3.8 or newer
- A valid API key from either:
  - Azure OpenAI resource, or
  - OpenAI (e.g. `https://platform.openai.com`)
- A deployed model (`gpt-4`, `gpt-4o`, or custom)

---

## 🔧 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/Alfred9/Natural-Language-Processing/edit/main/Medical-NER-App.git
cd Medical-NER-App
