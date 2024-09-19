from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("World's greatest chatbox")

input_text= st.text_input("Ask me anything")

promt=ChatPromptTemplate.from_messages(
    [("system","Your name is Viveka"),
    ("user","user query:{query}")
    ])

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = promt|llm|output_parser

if input_text:
    st.write(chain.invoke({"query":input_text}))
