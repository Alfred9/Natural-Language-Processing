import streamlit as st
from transformers import AutoModel
from numpy.linalg import norm

@st.cache_resource
def load_model():
    model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True, revision="bb64ef0192984bea83688b90f88572ff")
    return model

cos_sim = lambda a, b: (a @ b.T) / (norm(a) * norm(b))
model = load_model()

def compare_sentences(input_sentences, sentences):
    output = []
    for input_sentence in input_sentences:
        input_embedding = model.encode([input_sentence])[0]
        sentence_results = []
        for sentence in [s for s in sentences if s.strip()]:  # Filter out empty strings
            sentence_embedding = model.encode([sentence])[0]
            similarity = cos_sim(input_embedding, sentence_embedding)
            sentence_results.append((sentence, similarity))
        output.append((input_sentence, sentence_results))
    return output

def main():
    st.title("Sentence Similarity Comparison")

    input_sentences = st.text_area("Input Sentences", height=100).split("\n")
    sentences = st.text_area("Sentences to Compare", height=200).split("\n")

    if input_sentences and sentences:
        results = compare_sentences(input_sentences, sentences)
        st.subheader("Results")
        for input_sentence, sentence_results in results:
            st.write(f"Input Sentence: {input_sentence}")
            for sentence, similarity in sentence_results:
                st.write(f"{sentence} - Similarity: {similarity:.2f}")
            st.write("---")

if __name__ == "__main__":
    main()
