import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

st.title("Text Summarization with Streamlit")

user_text = st.text_area("Enter the text to be summarized : ", height=200)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-pro-latest")

prompt = '''You are an expert in summarization. 
Please provide a concise summary of the following text:
Text: 
'''

final_prompt = prompt + user_text

if user_text:
    response = model.generate_content(final_prompt)
    print("Output: ", response.text)
    st.write(response.text)
elif st.button("Summarize"):
    st.warning("Please enter some text to summarize.")