import streamlit as st
import time
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SystemMessage("Act like a human resource assistant"))

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Create the bar where we can type messages
prompt = st.chat_input("Poser une question ")

# Did the user submit a prompt?
if prompt:
    # Add the user's message to the chat history and display it
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(prompt))

    # Measure the start time
    start_time = time.time()

    # Generate response
    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=2
    )

    result = llm.invoke(st.session_state.messages).content

    # Measure the end time
    end_time = time.time()
    response_time = end_time - start_time

    # Display chatbot response and response time
    with st.chat_message("assistant"):
        st.markdown(result)
        st.markdown(f"⏱️ **Response Time:** {response_time:.2f} seconds")

    # Add AI response to chat history
    st.session_state.messages.append(AIMessage(result))
