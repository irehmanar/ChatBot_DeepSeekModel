# help to interect the llm model
# for custom prompts
from langchain_core.prompts import ChatPromptTemplate
# manage the display of response from llm
from langchain_core.output_parsers import StrOutputParser


from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv



load_dotenv()

#  for langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt  = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}"),
    ]
)


## streamlit framework

st.title('Langchain Demo With DeepSeek API')
input_text=st.text_input("Search the topic u want")



# ollama LLAma2 LLm 
llm=Ollama(model="deepseek-r1:1.5b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))
