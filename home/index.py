"""Home page shown when the user enters the application"""
import streamlit as st
import texts

def write():
    st.markdown("<h1 style='text-align: center;color:#585858;'><strong>Strojove uceni priklady</strong></h1>", unsafe_allow_html=True)

    text_agent =  texts.czechtext.text_agent()

    st.write(text_agent.text1)


if __name__ == "__main__":
    write()
