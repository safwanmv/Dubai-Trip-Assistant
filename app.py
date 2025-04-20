 # Imports
import os
from dotenv import load_dotenv
import openai
import streamlit as st

# Load Environment Variables
load_dotenv()  # This will load the API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initial System Message & Assistant Greeting
INITIAL_MESSAGE = [
    {
        "role": "system",
        "content": (
            "You are a trip planner in Dubai named Dubai Genie (DG). You're an expert in Dubai tourism, "
            "locations, food, events, and hotels. You respond professionally, ask users questions, and "
            "suggest day-wise itineraries. Responses must not exceed 200 words."
        )
    },
    {
        "role": "assistant",
        "content": "Hello, I am Dubai Genie, your expert trip planner. How can I help you today?"
    }
]


# Function to Get Response from OpenAI
def get_response_from_llm(messages):
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",  # You can choose the model version you need
        messages=messages
    )
    return response.choices[0].message.content

# Streamlit App Interface
st.title("🌆 Dubai Trip Assistant")

# Load or Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = INITIAL_MESSAGE.copy()

#  Display Chat Messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#  User Input Field
user_message = st.chat_input("Enter your message...")

#  Handle User Message
if user_message:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.chat_message("user"):
        st.markdown(user_message)

    # Show assistant typing...
    with st.chat_message("assistant"):
        with st.spinner("Dubai Genie is typing..."):
            response = get_response_from_llm(st.session_state.messages)
            st.markdown(response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

