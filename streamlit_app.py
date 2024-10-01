from sambaverse import parse_doc_universal

import streamlit as st
# Title of the app
st.title("PDF Uploader")

# File uploader widget for PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

source_type = 'github'
input_path = 'AR English 2023-24 Final (with cover).pdf'
additional_metadata = {'key': 'value'}
texts, metadata_list, langchain_docs = parse_doc_universal(uploaded_file,additional_metadata,source_type, additional_metadata)
for i in langchain_docs:
    st.writ(i)
    exit()
