import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gpt
from functions import *

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with gemini-2.5-flash!",
    page_icon=":robot_face:",
    layout="wide",
)

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in .env file")
    st.stop()

# Set up Google gemini-1.5-pro-latest AI model
try:
    gpt.configure(api_key=API_KEY)
    model = gpt.GenerativeModel('gemini-2.5-flash')
    
    # Initialize chat session
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
        
except Exception as e:
    st.error(f"❌ Error initializing Gemini: {str(e)}")
    st.stop()

# Display the chatbot's title
st.title("🤖 Chat with gemini-2.5-flash")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(map_role(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
if prompt := st.chat_input("Ask gemini-2.5-flash..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        response = fetch_gemini_response(prompt)
        st.markdown(response)