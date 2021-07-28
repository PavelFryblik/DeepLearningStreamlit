import streamlit as st
import os
import time
import pandas as pd
import numpy as np
from data.auxiliary_functions import Auxiliary

# from auxiliary_functions import Auxiliary

class DataLoad:

    pass

    # @st.cache(allow_output_mutation=True)
    # def get_connection():
    #     return create_engine(DataLoad.postgres)
    #
    # def load_df(table='',filters=[],dimensions=[],measures=[], query=''):
    #     if query == '':
    #         query = Auxiliary.query_processing(table=table,
    #                                            filters=filters,
    #                                            measures=measures,
    #                                            dimensions=dimensions)
    #
    #     with st.spinner('Loading Data...'):
    #         time.sleep(0.05)
    #         # print(query)
    #         df = pd.read_sql_query(query, DataLoad.get_connection())
    #     return df
    #
    # # @st.cache(allow_output_mutation=True)
    # def dataframe_load_and_persist(loading_dict, index='', sortascending='True', process='series', feature=''):
    #     df = DataLoad.load_df(**loading_dict)
    #     if index != '':
    #         df.sort_values(by=index, ascending=sortascending, inplace=True)
    #         df.set_index(index, inplace=True)
    #     df = DataLoad.processing_df(df, process=process)
    #     return df
    #
    #
    # def processing_df(df, process, feature='', sort=''):
    #     if process == 'value':
    #         if not df.empty:
    #             value =  df[feature].iloc[0]
    #         else:
    #             value = 0
    #     elif process == 'diff':
    #         if not df.empty:
    #             try:
    #                 if sort!='':
    #                     df = df.sort_values(by=sort,ascending=False)
    #                 df = df[feature].pct_change()
    #                 df = df.sort_values()
    #                 value =  round(df.iloc[0]*100, 2)
    #             except:
    #                 value = 0
    #         else:
    #             value = 0
    #     elif process == 'series':
    #         value = df
    #     elif process == 'diffseries':
    #         try:
    #             df = df.sort_values(by=sort)
    #             df[feature] = df[feature].pct_change()
    #             value = df
    #         except:
    #             df[feature] = 0
    #             value = df
    #     return value
    #
    # def to_filter(filters, filter_key):
    #     test=[]
    #     for filter in filters:
    #         test.append(filter)
    #     if test:
    #         filter_dict = {filter_key:test}
    #     else:
    #         filter_dict= {}
    #     return filter_dict
