import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
    )

# App framework
st.title('Find Relevant Fragments')
prompt = st.text_input('Plug in your query here')

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./VectorStore", embedding_function=embedding_function)

k = 3

# show to the screen if there is a prompt
if prompt:
    response = db.similarity_search(prompt, k=k)

    for i in range(k):
        title = response[i].metadata['Title']
        st.write(f'### Title: {title}')
        st.write(f'Article fragment: {response[i].page_content}')
        st.write('##')