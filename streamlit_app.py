import streamlit as st
import openai  # Assuming you're using OpenAI's GPT API

# Configure OpenAI API
openai.api_key = "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"  # Replace with your OpenAI API key

# GPT-3.5 model prompt
gpt3_prompt = "You are a helpful assistant."

# Function to generate response using GPT-3.5
def generate_response(user_input):
    prompt = f"{gpt3_prompt}\nUser: {user_input}\nAssistant:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Chat with GPT-3.5")
st.write("You are chatting with a GPT-3.5 powered assistant.")

user_input = st.text_input("You:", "")

if user_input:
    # Generate response using GPT-3.5
    response = generate_response(user_input)
    st.text_area("Assistant:", response, height=100)
