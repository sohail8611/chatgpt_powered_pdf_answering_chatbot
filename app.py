import os
import streamlit as st
from functions import *
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():

    st.title("D-DOT-PY Pdf+ChatGPT ")

    uploaded_file = st.file_uploader("Choose a PDF file to upload", type="pdf")
    if uploaded_file is not None:
        if st.button("Read PDF"):
            save_uploaded_file(uploaded_file)
            st.write("Please wait while we learn the PDF.")
            learn_pdf(uploaded_file.name)
            st.write("PDF reading completed! Now you may ask a question")
            os.remove(uploaded_file.name)
    user_input = st.text_input("Enter your Query:")

    if st.button("Send"):
        st.write("You:", user_input)
        response = Answer_from_documents(user_input)
        st.write("Bot: "+response)


if __name__ == "__main__":
    main()
