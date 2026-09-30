import streamlit as st
from llm_service import ChatService

st.set_page_config(
    page_title="woo hoo",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="expanded"
)


st.title("Welcome!")

if"messages" not in st.session_state:
  st.session_state.messages=[]

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

chat_service = ChatService(model="llama3.2:3b")

prompt=st.chat_input("What is your question?")
if prompt:
  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)



  handler=chat_service.generate_stream(st.session_state.messages)
  response=""
  with st.chat_message("assistant"):
    response_placeholder=st.empty()
    for chunk in handler:
      response+=chunk['message']['content']
      response_placeholder.markdown(response+"▌")
    response_placeholder.markdown(response)
  st.session_state.messages.append({"role":"assistant","content":response})
