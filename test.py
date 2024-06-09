import streamlit as st

st.title('Welcome to Sumans Virtual home')

st.write("Hello World")

name = st.text_input("Enter your name")

if x:= st.chat_input():
   st.chat_message("ai").write(x)

if(st.button('Submit')):
    result = name.title()
    st.success(result)