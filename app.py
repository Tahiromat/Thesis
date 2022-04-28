import pandas as pd
from prometheus_client import Histogram
import streamlit as st
from streamlit_option_menu import option_menu

from App_Pages.streamlit_page_helper_methods import city_names
from App_Pages.home_page import home_page
from App_Pages.visualization_page import line_visualization_page
from App_Pages.visualization_page import scatter_visualization_page

from Algorithms.Prophet_4_Forecast import prophet_for_forecast

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
CITY_NAMES_FOR_SIDE_BAR = city_names(MAIN_FOLDER_PATH)

with st.sidebar:
    selected_city = st.sidebar.selectbox('Select the city you want to review.', CITY_NAMES_FOR_SIDE_BAR)

def load_data(city_name):
    return city_name
data = load_data(selected_city)

# # From here you will choose data set 
# df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
# print(df.columns)
# df = df[:-1]
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.sidebar:
    st.markdown("###")

    selected_page = option_menu(None, ["Home", "Visualization", "Forecasting", 'Anomaly Detection', 'Blogs'], 
        icons=['house', 'list-task', "list-task", 'list-task', 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Select Forecasting Algorithm")
    visualization_types = option_menu(None, ["Line", "Scatter"], 
        icons=['list-task', 'list-task'], 
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
    anomaly_detetection_algorithms = option_menu(None, ["LSTM", "ARIMA", 'AUTOENCODER'], 
        icons=['list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("###")

    st.write("Read Blogs ")
    blogs = option_menu(None, ["About Time Series", "About Prophet", "About LSTM", "About ARIMA", 'About AUTOENCODER'], 
        icons=['list-task', 'list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

if selected_page == "Home":
    st.write(data)
    home_page()

elif selected_page == "Visualization":

    if visualization_types == "Line":
        line_visualization_page()
    else:
        scatter_visualization_page()

elif selected_page == "Forecasting":

    st.title("Forecasting Page")

    if forecast_algorithms == "Prophet":
        st.write("Prophet algorithm has been choosed for forecasting")
        prophet_for_forecast()

    elif  forecast_algorithms == "LSTM":
        st.write("LSTM algorithm has been choosed for forecasting")

    elif  forecast_algorithms == "ARIMA":
        st.write("ARIMA algorithm has been choosed for forecasting")

    else :
        st.write("AUTOENCODER algorithm has been choosed for forecasting")

elif selected_page == 'Anomaly Detection':
    
    st.title("Anomaly Detection Page")

    if  anomaly_detetection_algorithms == "LSTM":
        st.write("LSTM algorithm has been choosed for anolay detection")

    elif  anomaly_detetection_algorithms == "ARIMA":
        st.write("ARIMA algorithm has been choosed for anolay detection")

    else :
        st.write("AUTOENCODER algorithm has been choosed for anolay detection")

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
