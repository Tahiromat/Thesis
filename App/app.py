import streamlit as st
import pandas as pd
from streamlit_page_helper_methods import city_names

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
CITY_NAMES_FOR_SIDE_BAR = city_names(MAIN_FOLDER_PATH)

st.write("""### Anomaly Detection in Air Quality of Turkey """)

st.sidebar.selectbox('Cities', CITY_NAMES_FOR_SIDE_BAR)

