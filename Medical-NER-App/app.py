import streamlit as st
import stanza
import pandas as pd
import PyPDF2
import docx
import tempfile
import os

def load_model():
    # Download and initialize the MIMIC pipeline with i2b2 NER model
    try:
        # Add a check to see if the model is already downloaded
        import os
        model_dir = os.path.expanduser('~/stanza_resources/')
        if not os.path.exists(os.path.join(model_dir, 'en', 'mimic', 'ner', 'i2b2')):
            st.info("Downloading model for the first time. This may take a few minutes...")
        stanza.download('en', package='mimic', processors={'ner': 'i2b2'}, verbose=True)
        nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'}, verbose=True)
        return nlp
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.info("If the error persists, please contact the administrator. The app might need more resources to download and run the model.")
        return None

def process_text_with_stanza(text, nlp):
    # Process text through Stanza
    doc = nlp(text)
    
    # Extract entities
    entities = []
    for ent in doc.entities:
        entities.append({
            'word': ent.text,
            'entity_group': ent.type
        })
    
    return entities

def display_ner_results(text, entities):
    # Display the results in the format requested
    result_text = f"Input: {text}\n"
    for entity in entities:
        result_text += f"Text: {entity['word']} | Label: {entity['entity_group']}\n"
    result_text += "-" * 50
    return result_text

def read_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def main():
    st.set_page_config(
        page_title="Medical NER App",
        page_icon="🏥",
        layout="wide"
    )
    
    st.title("Medical Named Entity Recognition")
    st.markdown("""
    Extract medical entities from your clinical text using Stanza with the MIMIC/i2b2 model.
    
    ### Features:
    - Identifies medical entities such as problems, treatments, tests, and more
    - Processes text from direct input, PDFs, or Word documents
    - Based on the clinical NLP model from i2b2
    """)
    
    # Show sample text button
    if st.button("Load Sample Text"):
        sample_text = "The patient was a 56-year-old female admitted on 5/12/2021 with chief complaint of chest pain. History of diabetes mellitus, hypertension, and COPD. ECG showed normal sinus rhythm. Labs revealed elevated troponin at 0.12. Patient was treated with aspirin 325mg, Plavix 75mg, and IV heparin. Echo showed preserved EF of 60% with mild MR."
        st.session_state['text_input'] = sample_text
    
    # Load model
    @st.cache_resource
    def get_model():
        return load_model()
    
    nlp = get_model()
    
    if nlp is None:
        st.error("Could not load the NER model. Please check your installation of Stanza.")
        st.stop()
    
    # Create columns for layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Input method selection
        input_method = st.radio(
            "Choose input method:",
            ["Text Input", "File Upload"]
        )
        
        text_to_process = None
        
        if input_method == "Text Input":
            if 'text_input' not in st.session_state:
                st.session_state['text_input'] = ""
                
            text_input = st.text_area(
                "Enter medical text:",
                height=200,
                value=st.session_state['text_input'],
                placeholder="Example: The patient had a sore throat and was treated with Cepacol lozenges."
            )
            if text_input.strip():
                text_to_process = text_input
                
        else:  # File Upload
            uploaded_file = st.file_uploader(
                "Upload a file", 
                type=["pdf", "docx", "txt"],
                help="Supported formats: PDF, Word, TXT"
            )
            
            if uploaded_file is not None:
                try:
                    with st.spinner("Reading file..."):
                        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_file_path = tmp_file.name
                            
                    file_type = uploaded_file.name.split('.')[-1].lower()
                    if file_type == 'pdf':
                        text_to_process = read_pdf(tmp_file_path)
                    elif file_type == 'docx':
                        text_to_process = read_docx(tmp_file_path)
                    elif file_type == 'txt':
                        with open(tmp_file_path, 'r', encoding='utf-8') as f:
                            text_to_process = f.read()
                    
                    # Clean up the temp file
                    os.unlink(tmp_file_path)
                    
                    st.success("File successfully read!")
                    with st.expander("Show extracted text"):
                        st.text(text_to_process)
                    
                except Exception as e:
                    st.error(f"Error reading file: {str(e)}")
                    text_to_process = None
        
        process_button = st.button("Extract Entities")
    
    # Process and display results
    if process_button and text_to_process:
        with st.spinner("Processing text with Stanza MIMIC/i2b2 model..."):
            try:
                # Process text with Stanza
                entities = process_text_with_stanza(text_to_process, nlp)
                
                with col1:
                    # Display in the requested format
                    st.subheader("NER Results:")
                    st.code(display_ner_results(text_to_process, entities), language="text")
                
                with col2:
                    # Display info about the model
                    st.subheader("About the Model")
                    st.info("""
                    **Stanza MIMIC/i2b2 Model**
                    
                    This model is specifically designed for biomedical and clinical text processing. 
                    It's trained on the i2b2 dataset which focuses on identifying:
                    
                    - **PROBLEM**: Medical problems/conditions
                    - **TREATMENT**: Treatments, medications, procedures
                    - **TEST**: Diagnostic tests and measures
                    """)
                    
                    # Display entity statistics
                    if entities:
                        entity_types = {}
                        for entity in entities:
                            entity_type = entity['entity_group']
                            if entity_type in entity_types:
                                entity_types[entity_type] += 1
                            else:
                                entity_types[entity_type] = 1
                        
                        st.subheader("Entity Statistics")
                        stats_df = pd.DataFrame({
                            'Entity Type': list(entity_types.keys()),
                            'Count': list(entity_types.values())
                        })
                        st.bar_chart(stats_df.set_index('Entity Type'))
                    
                    # Display tabular data
                    st.subheader("Extracted Entities:")
                    if entities:
                        df = pd.DataFrame([{
                            'Entity': entity['word'],
                            'Type': entity['entity_group']
                        } for entity in entities])
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.info("No medical entities found in the text.")
            except Exception as e:
                st.error(f"Error processing text: {str(e)}")
                st.info("Try with a shorter text sample if the error persists.")

if __name__ == "__main__":
    main()
