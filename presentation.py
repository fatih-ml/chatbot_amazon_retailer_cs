import streamlit as st


def show_presentation():
    st.write("## Introduction")
    st.write(
        """
        Welcome to the Amazon Seller Virtual Assistant project! 
        This project aims to build a chatbot for Amazon sellers, 
        addressing various issues related to selling on Amazon such as logistics, marketing, and more.

        This is an educational study for experimental purposes and not a fully-fledged chatbot solution. 
        The goal is to explore and demonstrate the use of modern NLP and deployment tools.
        """
    )

    st.write("## Project Overview")
    st.write(
        """
    We have visited `15 valuable pages` on Amazon Seller Central and captured PDF samples of those pages. 
    Importantly, we also composed metadata such as titles, subtitles, and topics for these pages. 
    Here is a high-level overview of the steps involved:
    """
    )

    st.image("images/image1.png", caption="Data Sources")

    st.write(
        """
    `Document Collection:` Collected PDFs from 15 pages on Amazon Seller Central.  
    `Metadata Composition:` Composed metadata for each document.  
    `Data Extraction:` LlamaParse for parsing, added metadata, a single JSON format.  
    `Indexing and Vectorization:` Llama Index's VectorStoreIndex to vectorization and indexing.   
    `Text Generation:` Utilized OpenAI's GPT-3.5 Turbo model for generating responses   
    `Deployment:` Deployed the chatbot using Streamlit for a user-friendly interface.  
        """
    )

    st.image("images/image2.png", caption="Data Processing")

    st.write("## Architecture")
    st.write(
        """The chatbot uses a VectorStoreIndex and Document objects from LlamaIndex to manage and retrieve information. 
        On the other hand, OpenAI's GPT3.5-Turbo model utilized for reasoning and text generation.
        """
    )

    st.image("images/image3.png", caption="RAG Architecture")


if __name__ == "__main__":
    show_presentation()
