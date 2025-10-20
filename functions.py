import streamlit as st

# Function to translate roles between Gemini and Streamlit terminology
def map_role(role):
    if role == "model":
        return "assistant"
    else:
        return role

def fetch_gemini_response(user_query):
    try:
        # Use the session's model to generate a response
        response = st.session_state.chat_session.send_message(user_query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"