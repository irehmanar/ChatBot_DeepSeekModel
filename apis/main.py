from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

#  for langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


app = FastAPI (
    title='Langchain Server',
    description='A simple API for demonstrating Langchain capabilities',
    version='1.0'
)


# Initialize Ollama model
llm=Ollama(model="deepseek-r1:1.5b")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")


# Add routes
add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
