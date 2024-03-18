import streamlit as st
from openai import OpenAI
client = OpenAI()

# Set your OpenAI API key
OpenAI.api_key = ""

# User input field
user_input = st.text_input("Ask me anything!")

if user_input:
    completion = client.chat.completions.create( # Change the method name
        model = 'gpt-3.5-turbo-0125',
        messages = [ # Change the prompt parameter to messages parameter
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {'role': 'user', 'content': user_input}
        ],
        temperature = 0  
    )

    # Display the chatbot response
    st.write(completion.choices[0].message.content)
    st.session_state["user_input"] = ""