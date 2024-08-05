import streamlit as st
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


st.title("Chat-bot")
with st.chat_message("assistant"):
    st.write("👋hello")

#initialize the history list/stack
if 'messages' not in st.session_state:
    st.session_state.messages=[]  #incase of a reload empty session starts

#display the chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])    


def generate_reponse(prompt):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system","content":"you are a chatbot"},
        {"role":"user","content":prompt}
    ],
    temperature=1,
    max_tokens=512
    )
    return completion.choices[0].message.content


if prompt:=st.chat_input():  
    with st.chat_message("User"):
        st.markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})   

    with st.chat_message("assistant"):
        with st.spinner("Thinking"):
            res=generate_reponse(prompt)
            st.markdown(res)
    st.session_state.messages.append({'role':'assistant','content':res})        