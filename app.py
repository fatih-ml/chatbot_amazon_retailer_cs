import os
from dotenv import load_dotenv
import streamlit as st
import openai
import pinecone

# Load environment variables from .env file
load_dotenv()

# Access the API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Set API keys for the respective services
openai.api_key = OPENAI_API_KEY
pinecone.init(api_key=PINECONE_API_KEY)