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

