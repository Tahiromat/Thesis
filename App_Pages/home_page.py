import streamlit as st 
from plotly import graph_objs as go 

from App_Pages.generate_data_basedon_selections import find_data

DATASET_PATH = 'Dataset/'

def home_page():
    st.title("""Air Quality of Turkey """)
    
    data = find_data(DATASET_PATH)

    part_of_data = data.loc[data['Date'] < '2021-10-18']
    
    # total_column_names = data.columns
    # total_column_names = total_column_names[1:]
    st.write(data.tail())
    # st.write(data.info())
    st.write(part_of_data)
