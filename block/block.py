# from elements import Streamlit_elements
import streamlit as st
import pandas as pd
import time
import altair as alt
import numpy as np
from distutils.version import StrictVersion
from package.components import add_w
from datetime import datetime, date, timedelta

from data.data import DataLoad
from data.auxiliary_functions import Auxiliary
from elements.elements import Streamlit_elements


class Block:
    def block_digits_anonymous_per_game(df, measure, filter_index_value='', format='.2%'):
        list_steamelement = st.beta_columns((1,1,1,1))
        list = ['']

        formatn = '{:'+ format +'}'
        for gameindex, game in enumerate(list):
            steamelement = list_steamelement[gameindex]
            gamename = Block.games[game]
            if filter_index_value == '':
                dfgame = df[df['game']==game]
                try:
                    num1 = (float(dfgame[measure].tail(1).iloc[0])/float(dfgame[measure].tail(2).iloc[0]) - 1)
                except:
                    num1 = 0
                Streamlit_elements.mymarkdown(object=steamelement,
                                              number=formatn.format(num1),
                                              text=gamename)
