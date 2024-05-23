# Chatbot Amazon Seller Assistant

Welcome to the Chatbot Amazon Seller Assistant project! This project aims to build a chatbot for Amazon sellers, addressing various issues related to selling on Amazon such as logistics, marketing, and more.

This is an educational study for experimental purposes and not a fully-fledged chatbot solution. The goal is to explore and demonstrate the use of modern NLP and deployment tools.

## Project Overview

We have visited 15 valuable pages on Amazon Seller Central and captured PDF samples of those pages. Importantly, we also composed metadata such as titles, subtitles, and topics for these pages. Here is a high-level overview of the steps involved:

1. **Document Collection**: Collected PDFs from 15 pages on Amazon Seller Central.
2. **Metadata Composition**: Composed metadata for each document.
3. **Data Extraction**: Used LlamaParse to extract these documents into markdown format and rearranged metadata and markdown files into a single JSON format.
4. **Indexing and Vectorization**: Used Llama Index's VectorStoreIndex to vectorize, cache, and index the data for later use in retrieval queries.
5. **Text Generation**: Utilized OpenAI's GPT-3.5 Turbo model for generating responses based on retrieved data.
6. **Deployment**: Deployed the chatbot using Streamlit for a user-friendly interface.

## Setup and Run the Chatbot

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- LlamaParse API key (with 1000 pages free daily usage)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/fatih-ml/chatbot_amazon_seller_assistant.git
   cd chatbot_amazon_seller_assistant
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Setup OpenAI API key:

   Create a .streamlit directory and add a secrets.toml file with your OpenAI API key.

   ```bash
    # .streamlit/secrets.toml
    [openai]
    api_key = "your_openai_api_key"
   ```

4. Setup LlamaParse API key:

   Ensure you have your LlamaParse API key set up according to their documentation. Not neccessary for use this repo, but incase you want to add documents, you will need a key.

   **Running the Application**  
    To run the Streamlit application, execute the following command:

   ```bash
   streamlit run app.py
   ```

## Observations

Through this project, we observed that the accuracy of the answers provided by the chatbot significantly improved by adding relevant metadata to the documents. This metadata enrichment helped in better context understanding and response generation.

## Contributing

We welcome contributions and suggestions! Feel free to fork this repository and submit pull requests.

## Contact

For any questions or further information, you can reach out to me on [LinkedIn](https://www.linkedin.com/in/fatih-calik-ml/).

Thanks for reading and visiting our repo! We hope this project serves as a helpful educational resource.
