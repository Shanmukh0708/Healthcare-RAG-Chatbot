import streamlit as st
from utils.rag_helper import RAGHelper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Healthcare RAG Chatbot",
    page_icon="🏥",
    layout="wide"
)

# Initialize RAG helper
@st.cache_resource
def initialize_rag():
    rag_helper = RAGHelper()
    vectorstore = rag_helper.create_vectorstore("data/healthcare_info.txt")
    rag_chain = rag_helper.get_rag_chain(vectorstore)
    return rag_helper, rag_chain

rag_helper, rag_chain = initialize_rag()

# Main interface
st.title("Healthcare RAG Chatbot")
st.write("Compare responses between regular AI and RAG-enhanced AI for healthcare queries")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
user_input = st.text_input("Ask a healthcare-related question:")

if user_input:
    # Get both regular and RAG responses
    try:
        # Regular response
        regular_response = rag_helper.get_regular_response(user_input)
        
        # RAG response
        rag_response = rag_chain({"question": user_input})
        
        # Store in session state
        st.session_state.messages.append({"question": user_input, 
                                        "regular": regular_response, 
                                        "rag": rag_response['answer']})
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display chat history
for message in st.session_state.messages:
    st.write("---")
    st.write("❓ **Your Question:**", message["question"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("🤖 **Regular AI Response:**")
        st.write(message["regular"])
    
    with col2:
        st.write("🔍 **RAG-Enhanced Response:**")
        st.write(message["rag"])

# Add some helpful information
with st.sidebar:
    st.title("About")
    st.write("""
    This healthcare chatbot demonstrates the difference between:
    1. Regular AI responses
    2. RAG-enhanced responses
    
    RAG (Retrieval Augmented Generation) enhances responses by:
    - Using specific healthcare knowledge
    - Providing more accurate information
    - Reducing hallucinations
    """)