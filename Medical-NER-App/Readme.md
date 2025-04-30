#  Medical NER App

This is a simple Python app that extracts biomedical entities (e.g., diseases, drugs, symptoms, treatments) from clinical notes using large language models.

You can run it using:
- **Azure OpenAI Service** (recommended for enterprise or cloud deployment), or
- **OpenAI API** (via direct API key from OpenAI)

---

##  Features

- Extracts structured entities in JSON format from clinical text
- Built-in support for `gpt-4o`, `gpt-4`, or your own Azure OpenAI deployment
- Uses structured prompts to improve model consistency
- Includes logging and error handling
- Easy to run locally via CLI

---

## Requirements

- Python 3.8 or newer
- A valid API key from OpenAiI 
- A deployed model (`gpt-4`, `gpt-4o`, or custom)

---

## Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/Alfred9/Natural-Language-Processing/edit/main/Medical-NER-App.git
cd Medical-NER-App
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # on Windows use: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file in the root directory and fill it with one of the following:

#### For **Azure OpenAI**:

```env
OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
MODEL_DEPLOYMENT_ID=gpt-4o  # or your deployment name
```

#### For **OpenAI** (non-Azure):

```env
OPENAI_API_KEY=your-openai-api-key
USE_OPENAI_DIRECT=true
```

> ⚠ Make sure to use the correct API key and endpoint depending on your provider.

---

##  Running the App Locally

Run the app with:

```bash
python ner.py
```

You should see output like:

```json
{
  "diseases": ["hypertension"],
  "drugs": ["lisinopril"],
  "symptoms": [],
  "treatments": []
}
```

---

##  Example Input and Output

**Input clinical note:**
```
Patient diagnosed with hypertension and prescribed lisinopril.
```

**Output JSON:**
```json
{
  "diseases": ["hypertension"],
  "drugs": ["lisinopril"],
  "symptoms": [],
  "treatments": []
  "Tests": []
}
```

---

## Project Structure

```
.
├── ner.py             # Main Python script
├── .env               # Environment variables 
├── requirements.txt   # Python dependencies
└── README.md          # Project instructions
```

Install them via:

```bash
pip install -r requirements.txt
```
## 📄 License

MIT License — feel free to use and adapt for personal or commercial projects. Attribution appreciated.
