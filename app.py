import streamlit as st
from rag.chain import rag_chain

st.title("🦜🔗 Langchain Quickstart App")

def generate_response(input_text):
    st.info(rag_chain.invoke(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    generate_response(text)