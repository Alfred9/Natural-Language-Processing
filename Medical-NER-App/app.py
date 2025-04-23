import streamlit as st
import json
from ner import extract_entities
import PyPDF2 # type: ignore
from docx import Document # type: ignore
from io import BytesIO

st.title("Biomedical NER App")

st.header("Input Clinical Note")
input_method = st.radio("Choose input method:", ("Text", "Upload PDF", "Upload Word Document"))

clinical_note = ""

if input_method == "Text":
    clinical_note = st.text_area("Enter Clinical Note",
                                 placeholder="e.g., Patient diagnosed with hypertension and prescribed lisinopril.")
elif input_method == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            clinical_note = text.strip()
            st.text_area("Extracted Text", clinical_note, height=200)
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
elif input_method == "Upload Word Document":
    uploaded_file = st.file_uploader("Upload a Word document", type=["docx"])
    if uploaded_file:
        try:
            doc = Document(BytesIO(uploaded_file.read()))
            text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
            clinical_note = text.strip()
            st.text_area("Extracted Text", clinical_note, height=200)
        except Exception as e:
            st.error(f"Error reading Word document: {str(e)}")

if st.button("Extract Entities"):
    if not clinical_note:
        st.error("Please provide a clinical note via text or file upload.")
    else:
        try:
            entities = extract_entities(clinical_note)

            st.subheader("Extracted Entities")
            st.json(entities)

            for category, items in entities.items():
                st.write(f"**{category.capitalize()}:** {', '.join(items) if items else 'None'}")

        except ValueError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")

st.sidebar.header("Example Clinical Notes")
st.sidebar.write("1. Patient diagnosed with hypertension and prescribed lisinopril.")
st.sidebar.write("2. Complains of chest pain and fatigue, treated with aspirin.")
