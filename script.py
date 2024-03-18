import os
import openai
import streamlit as st

# Load your OpenAI API key from an environment variable
api_key = os.getenv('OPENAI_API_KEY')
if api_key is not None:
    openai.api_key = api_key
else:
    st.error('OpenAI API key not found. Please set it as an environment variable.')
    st.stop()

# Initialize Streamlit application
st.title("Adira Chatbot")

# User input field
user_input = st.text_input("Ask me anything!")

if user_input:
    # Make a request to the OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo-0125',
            messages=[
                {"role": "system", "content": "You are a helpful tech support chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Display the chatbot response
        st.write(response.choices[0].message['content'])

    except openai.OpenAIError as e:
        st.error(f"An error occurred: {e}")
