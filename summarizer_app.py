import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Summarizer", layout="centered")

st.title("📝 Text Summarizer using Hugging Face")

text = st.text_area("Enter your long text here", height=300)

if st.button("Summarize"):
    with st.spinner("Summarizing..."):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        st.success("Summary:")
        st.write(summary)
