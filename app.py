import streamlit as st
from streamlit_option_menu import option_menu

from App_Pages.home_page import *
from App_Pages.visualization_page import *
from App_Pages.forecasting_page import *
from App_Pages.anomaly_detection_page import *

DATASET_PATH = 'Dataset/'

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# with st.sidebar:
#     find_data(DATASET_PATH)
    # selected_city = st.sidebar.selectbox('Select the city you want to review.', CITY_NAMES_FOR_SIDE_BAR)

with st.sidebar:
    # st.markdown("###")

    selected_page = option_menu(None, ["Home", "Visualization", "Forecasting", 'Anomaly Detection', 'Blogs'], 
        icons=['house', 'list-task', "list-task", 'list-task', 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Select Visualization Type")
    visualization_types = option_menu(None, ["Line", "Scatter", "Histogram"], 
        icons=['list-task', 'list-task', 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Select Forecasting Algorithm")
    forecast_algorithms = option_menu(None, ["Prophet", "LSTM", "ARIMA", 'AUTOENCODER'], 
        icons=['list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Select Anomaly Detection Algorithm")
    anomaly_detetection_algorithms = option_menu(None, ["LSTM", "PyCaret", 'Prophet'], 
        icons=['list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Read Blogs ")
    blogs = option_menu(None, ["About Time Series", "About Prophet", "About LSTM", "About ARIMA", 'About AUTOENCODER'], 
        icons=['list-task', 'list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

if selected_page == "Home":
    # st.write(data)
    home_page()

elif selected_page == "Visualization":

    if visualization_types == "Line":
        st.title("Line Visualization")
        line_visualization_page()

    elif visualization_types == "Scatter":
        st.title("Scatter Visualization")
        scatter_visualization_page()

    else:
        st.title("Histogram Visualization")
        histogram_visualization_page()

elif selected_page == "Forecasting":

    st.title("Forecasting Page")

    if forecast_algorithms == "Prophet":
        prophet_forecasting_page()

    elif  forecast_algorithms == "LSTM":
        lstm_forecasting_page()

    elif  forecast_algorithms == "ARIMA":
        arima_forecasting_page()

    else :
        autoencoder_forecasting_page()

elif selected_page == 'Anomaly Detection':
    
    st.title("Anomaly Detection Page")

    if  anomaly_detetection_algorithms == "LSTM":
        lstm_anomaly_detection_page()
        
    elif  anomaly_detetection_algorithms == "PyCaret":
        pycaret_anomaly_detection_page()

    else :
        prophet_anomaly_detection_page()

else:

    if blogs == "About Time Series":
        st.title("About Time Series")

    elif blogs == "About Prophet":
        st.title("About Prophet")

    elif blogs == "About LSTM":
        st.title("About LSTM")

    elif blogs == "About ARIMA":
        st.title("About ARIMA")

    else:
        st.title("About AUTOENCODER")
