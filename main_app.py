import streamlit as st
import SessionState as ss

import classification.index
import home.index

from block.block import Block
from elements.elements import Streamlit_elements
from data.data import DataLoad
from data.auxiliary_functions import Auxiliary

import package
import texts

GENERAL_PAGES = {
    "Home": home.index,
    "Klasifikace": classification.index,
}


st.set_page_config(
    page_title="|Machine|Learning|",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():

    state = ss._get_state()

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(GENERAL_PAGES.keys()))

    page = GENERAL_PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        package.components.write_page(page)

    state.sync()

if __name__ == "__main__":
    main()
