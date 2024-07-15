import streamlit as st
import requests
import json
import random

# Set page config
st.set_page_config(page_title="Sage - First Aid. Simplified", page_icon="👩‍⚕️", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        color: #ffffff;
    }
    .chat-message.user {
        background-color: #2b5797;
    }
    .chat-message.bot {
        background-color: #1e3d59;
    }
    .chat-message .avatar {
      width: 20%;
    }
    .chat-message .avatar img {
      max-width: 78px;
      max-height: 78px;
      border-radius: 50%;
      object-fit: cover;
    }
    .chat-message .message {
      width: 80%;
      padding: 0 1.5rem;
    }
    h1, h2, h3 {
        color: #4CAF50;
    }
    .stAlert > div {
        color: #ffffff;
        background-color: #1e222a;
    }
    </style>
    """, unsafe_allow_html=True)

# Mistral API key
api_key = "l6bZOZPgRwKfPA9j88jI2yFNFumkXDXW"

# Mistral API endpoint
api_url = "https://api.mistral.ai/v1/chat/completions"

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def get_ai_response(user_input):
    try:
        prompt = f"""You are Sage, an empathetic AI health companion. Engage in a natural conversation with the user, addressing their health concerns or general queries. If they greet you, respond warmly and ask about their well-being. If they describe symptoms or health issues, provide helpful advice.

User input: {user_input}

Respond in a conversational manner, showing empathy and care. If health advice is needed, include:

1. Potential causes or diagnoses
2. Immediate actions or remedies
3. Lifestyle or dietary suggestions
4. When to seek professional medical help

Always prioritize the user's safety and well-being in your responses."""

        data = {
            "model": "mistral-tiny",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }

        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "I'm sorry, but I couldn't generate a response. Could you please try rephrasing your question?"

    except Exception as e:
        return f"I apologize, but an error occurred while processing your request. Please try again later. Error: {str(e)}"

# Health tips
health_tips = [
    "Stay hydrated! Aim for 8 glasses of water a day.",
    "Practice mindfulness or meditation for 10 minutes daily.",
    "Take short breaks every hour if you sit for long periods.",
    "Incorporate colorful fruits and vegetables into your meals.",
    "Aim for 7-9 hours of sleep each night.",
    "Practice good hand hygiene to prevent infections.",
    "Stand up and stretch every hour to improve circulation.",
    "Try to get at least 30 minutes of moderate exercise daily.",
    "Limit processed foods and choose whole foods instead.",
    "Take time to relax and de-stress each day."
]

# Title and description
st.title("🧠 Sage: First Aid Simplified")
st.markdown("Your AI-powered health assistant for friendly advice and personalized health insights. Remember, in emergencies, always call your local emergency number immediately.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Chat with Sage..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_ai_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.image("C:/Users/shash/OneDrive/Desktop/Sage/SAGE.jpeg", width=300)
    st.title("About Sage")
    st.markdown(
        """
        Sage is your advanced AI-powered health companion. It provides:
        
        - Friendly, conversational health advice
        - Potential causes and immediate actions
        - Lifestyle and dietary suggestions
        - Guidance on when to seek professional help
        
        **Remember:** While Sage offers helpful guidance, it's not a 
        substitute for professional medical care. Always consult with
        healthcare professionals for personalized medical advice.
        
        Stay informed, stay healthy!
        """
    )
    st.warning("This is a demo application. The advice provided should not be considered as professional medical advice.")
    
    # Daily Health Tip
    st.subheader("🌟 Daily Health Tip")
    st.info(random.choice(health_tips))

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ by Shashank Guda & Bhumika Dasari | © 2024 Sage Health")