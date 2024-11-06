import streamlit as st
import pandas as pd
from docx import Document
import requests
from io import BytesIO

# GitHub raw URLs for your files (replace with your actual URLs)
EXCEL_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/data.xlsx"
DOCX_URL = "https://github.com/Iamkrmayank/Master_Library/blob/main/Master%20Library.docx"

# Function to load and display Excel file from GitHub
def display_excel_from_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        excel_data = BytesIO(response.content)
        df = pd.read_excel(excel_data)
        st.write("### Excel File Content")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading Excel file from GitHub: {e}")

# Function to load and display DOCX file from GitHub
def display_docx_from_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        docx_data = BytesIO(response.content)
        doc = Document(docx_data)
        content = "\n".join([para.text for para in doc.paragraphs])
        st.write("### DOCX File Content")
        st.text(content)
    except Exception as e:
        st.error(f"Error reading DOCX file from GitHub: {e}")

# Streamlit app
st.title("Display Excel and DOCX Files from GitHub Repository")

# Display Excel file content
st.write("Fetching and displaying the Excel file from GitHub:")
display_excel_from_github(EXCEL_URL)

# Display DOCX file content
st.write("Fetching and displaying the DOCX file from GitHub:")
display_docx_from_github(DOCX_URL)
