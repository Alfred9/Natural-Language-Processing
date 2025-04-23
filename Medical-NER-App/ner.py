import os
import json
import logging
from openai import AzureOpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT', 'https://bioner.openai.azure.com/')
deployment_id = os.getenv('MODEL_DEPLOYMENT_ID', 'gpt-4o')

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-02-15-preview"
)

def extract_entities(clinical_note: str) -> dict:
    """
    Extract biomedical entities from a clinical note using Azure OpenAI.
    Returns a dictionary of extracted entities.
    """
    try:
        if not clinical_note:
            logger.warning("No clinical note provided.")
            raise ValueError("Clinical note cannot be empty.")

        logger.info(f"Processing clinical note: {clinical_note[:100]}...")

        response = client.chat.completions.create(
            model=deployment_id,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Biomedical NER assistant. Extract entities such as diseases, drugs, symptoms, "
                        "and treatments from the clinical note provided by the user. ONLY return a valid JSON object "
                        "in this format:\n\n"
                        "{\n"
                        "  \"Symptoms\": [],\n"
                        "  \"Diseases\": [],\n"
                        "  \"Tests\": []\n"
                        "  \"Treatments\": []\n"
                        "  \"Drugs\": [],\n"
                        "}\n\n"
                        "Do not add any explanation or commentary."
                    )
                },
                {"role": "user", "content": f"Clinical note: {clinical_note}"}
            ],
            max_tokens=500,
            temperature=0.0
        )

        response_text = response.choices[0].message.content.strip()
        logger.info(f"Raw response from model: {response_text}")

        try:
            extracted_entities = json.loads(response_text)
            logger.info(f"Extracted entities: {extracted_entities}")
            return extracted_entities
        except json.JSONDecodeError as e:
            logger.error(f"Model response not valid JSON: {response_text}")
            raise ValueError("Invalid JSON. Model said: " + response_text) from e

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise

if __name__ == "__main__":
    test_note = "Patient diagnosed with hypertension and prescribed lisinopril."
    try:
        result = extract_entities(test_note)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}")
