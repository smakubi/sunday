import streamlit as st

st.title("Sunday App")

simple_key = st.secrets["OPENAI_API_KEY"]
st.write(simple_key)

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
