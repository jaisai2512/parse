from sambaverse import parse_doc_universal

import streamlit as st
import os
# Title of the app
st.title("PDF Uploader")

# File uploader widget for PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

source_type = 'github'
with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Get the full path of the file
file_path = os.path.join("tempDir", uploaded_file.name)
additional_metadata = {'key': 'value'}
texts, metadata_list, langchain_docs = parse_doc_universal(file_path,additional_metadata,source_type, additional_metadata)
for i in langchain_docs:
    st.writ(i)
    exit()
