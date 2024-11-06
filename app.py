import streamlit as st
import pandas as pd
from docx import Document

# Function to read Excel file and display content
def display_excel(file):
    try:
        # Read the Excel file
        df = pd.read_excel(file)
        st.write("### Excel File Content")
        st.dataframe(df)  # Display DataFrame in Streamlit
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")

# Function to read DOCX file and display content
def display_docx(file):
    try:
        # Read the DOCX file
        doc = Document(file)
        content = "\n".join([para.text for para in doc.paragraphs])
        st.write("### DOCX File Content")
        st.text(content)  # Display content in Streamlit
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")

# Streamlit app
st.title("Display Excel and DOCX Files")

# File upload for Excel
st.write("Upload an Excel file to display its content:")
excel_file = st.file_uploader("Choose an Excel file", type="xlsx")
if excel_file is not None:
    display_excel(excel_file)

# File upload for DOCX
st.write("Upload a DOCX file to display its content:")
docx_file = st.file_uploader("Choose a DOCX file", type="docx")
if docx_file is not None:
    display_docx(docx_file)
