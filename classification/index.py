"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st
from distutils.version import StrictVersion

from datetime import datetime, timedelta
from block.block import Block
from elements.elements import Streamlit_elements
from data.data import DataLoad
from data.auxiliary_functions import Auxiliary
import package

import pandas as pd

from . import helloworld as helloworld

def write():

    dashes = ['','Prvni vzkaz od stroje']

    dashnum = st.selectbox('Dashboard', dashes)

    if dashnum == 'Prvni vzkaz od stroje':
        package.components.write_page(helloworld)

if __name__ == "__main__":
    write()
