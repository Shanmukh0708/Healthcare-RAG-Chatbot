# Healthcare-RAG-Chatbot


## Table of Contents

*   [Introduction](#introduction)
*   [Features](#features)
*   [How it Works](#how-it-works)
*   [Setup and Installation](#setup-and-installation)
    *   [Prerequisites](#prerequisites)
    *   [Installation Steps](#installation-steps)
*   [Usage](#usage)


## Introduction

The Healthcare RAG Chatbot is an interactive Streamlit application designed to demonstrate the power of Retrieval Augmented Generation (RAG) in providing accurate and contextually relevant answers to healthcare-related queries. This chatbot allows users to compare responses from a regular AI model with those from a RAG-enhanced AI, highlighting how RAG leverages specific domain knowledge to reduce hallucinations and improve factual accuracy.

## Features

*   **Dual Response Comparison:** Simultaneously displays responses from a regular AI and a RAG-enhanced AI for the same query.
*   **RAG Enhancement:** Utilizes a pre-defined healthcare knowledge base (`healthcare_info.txt`) to augment AI responses.
*   **Interactive Chat Interface:** A user-friendly Streamlit interface for asking questions and viewing chat history.
*   **Session Management:** Maintains chat history within the current session.
*   **Clear Distinction:** Visually separates regular AI responses from RAG-enhanced responses.
*   **Scalable Knowledge Base:** Easily extendable by modifying the `healthcare_info.txt` file.

## How it Works

The application operates on the following principles:

1.  **Knowledge Base Loading:** Upon initialization, the `healthcare_info.txt` file is loaded.
2.  **Text Splitting:** The loaded text is split into smaller, manageable chunks using `RecursiveCharacterTextSplitter`.
3.  **Embedding Generation:** These text chunks are then converted into numerical vector embeddings using `OpenAIEmbeddings`.
4.  **Vector Store Creation:** The embeddings are stored in a FAISS vector store, enabling efficient similarity searches.
5.  **RAG Chain Setup:** A `ConversationalRetrievalChain` is configured, linking a `ChatOpenAI` language model with the FAISS vector store and a `ConversationBufferMemory` for chat history.
6.  **User Query:** When a user enters a question:
    *   The **Regular AI** directly uses the `ChatOpenAI` model to generate a response.
    *   The **RAG-Enhanced AI** first retrieves relevant information from the FAISS vector store based on the user's query. This retrieved context is then provided to the `ChatOpenAI` model along with the original query, guiding the model to generate a more informed and accurate answer.
7.  **Display:** Both responses are displayed side-by-side in the Streamlit interface.





*   **`app.py`**: The main Streamlit application file. It sets up the UI, initializes the RAG helper, handles user input, and displays responses.
*   **`data/`**:
    *   **`healthcare_info.txt`**: Contains the domain-specific healthcare information used to build the RAG knowledge base.
    *   **`questions.txt`**: (Optional) A file containing example questions that can be used for testing or demonstration.
*   **`utils/`**:
    *   **`rag_helper.py`**: Contains the `RAGHelper` class, which encapsulates the logic for creating the vector store, setting up the RAG chain, and generating both regular and RAG-enhanced responses.
*   **`.env.example`**: A template for your environment variables file.
*   **`requirements_updated.txt`**: Lists all the Python dependencies required to run the project.
*   **`README.md`**: This file, providing an overview and instructions for the project.

## Setup and Installation

### Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.9+
*   An OpenAI API Key

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/healthcare-rag-chatbot.git
    cd healthcare-rag-chatbot
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements_updated.txt
    ```

4.  **Set up your OpenAI API Key:**

    *   Create a file named `.env` in the root directory of the project.
    *   Add your OpenAI API key to this file in the following format:

        ```
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
        Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

## Usage

To run the Streamlit application, execute the following command from the project's root directory:

```bash
streamlit run app.py
