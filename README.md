# Amazon Retailer Customer Service Chatbot

This project implements a customer service chatbot for an Amazon retailer using LangChain, LlamaParse, OpenAI's GPT-3.5 Turbo API, and deploys it on Streamlit. The chatbot uses provided PDF documents to handle customer queries.

## Requirements

- Python 3.11.9
- Streamlit
- LangChain
- LlamaParse (API Key needed)
- OpenAI (API Key needed)
- Pinecone-client (API Key needed)
- PyPDF2

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/fatih-ml/chatbot_amazon_retailer_cs.git
   cd chatbot_amazon_retailer_cs
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Replace API Keys with your, or create a config/env file to configure your API keys

2. Add your PDF documents to the `data` directory.

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Acknowledgements

- [LangChain](https://github.com/hwchase17/langchain)
- [LlamaParse](https://github.com/example/llamaparse)
- [OpenAI](https://openai.com)
- [Streamlit](https://streamlit.io)
- [Pinecone](https://www.pinecone.io)
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/)

## Contact

For any questions or issues, please contact..
