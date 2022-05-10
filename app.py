import streamlit as st
from App_Pages.home_page import *
from App_Pages.forecasting_page import *
from App_Pages.visualization_page import *
from streamlit_option_menu import option_menu
from App_Pages.anomaly_detection_page import *
from App_Pages.generate_data_basedon_selections import *

st.set_page_config(page_title="Air Quality Analysis", page_icon="❗", layout="wide")
st.markdown(""" <style> [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {width: 280px;} </style> """, unsafe_allow_html=True)
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
DATASET_PATH = 'Dataset/'

with  st.sidebar:
    st.title("Choose Type")
    st.markdown("This is an open source project which can be downloaded for free from github (requires developer experience to set up and configure)")
    st.markdown("#")
    data_path = find_data(st, DATASET_PATH)

with st.sidebar:
    st.markdown("###")
    selected_page = option_menu(None, ["Home", "Visualization", "Forecasting", 'Anomaly Detection', 'Blogs'], 
        icons=['house', 'list-task', "list-task", 'list-task', 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("#")
    st.write("Select Visualization Type")
    visualization_types = option_menu(None, ["Line", "Scatter", "Area Chart", "Histogram"], 
        icons=['list-task', 'list-task', 'list-task', 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("#")
    st.write("Select Forecasting Algorithm")
    forecast_algorithms = option_menu(None, ["Prophet", "LSTM", "ARIMA"], 
        icons=['list-task', 'list-task', "list-task"], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("#")
    st.write("Select Anomaly Detection Algorithm")
    anomaly_detetection_algorithms = option_menu(None, ["LSTM", "PyCaret", 'Prophet'], 
        icons=['list-task', 'list-task', "list-task", 'list-task'], 
        menu_icon="cast", default_index=0, orientation="vertical")

with st.sidebar:
    st.markdown("#")
    st.write("Read Blogs ")
    blogs = option_menu(None, ["About Time Series", "About Prophet", "About LSTM", "About ARIMA"], 
        icons=['list-task', 'list-task', 'list-task', "list-task"], 
        menu_icon="cast", default_index=0, orientation="vertical")

if selected_page == "Home":
    st.title("""Air Quality of Turkey """)
elif selected_page == "Visualization":
    st.title("Visualization")
elif selected_page == "Forecasting":
    st.title("Forecasting")
elif selected_page == 'Anomaly Detection':
    st.title("Anomaly Detection")
else:
    st.title("Blogs")

if selected_page == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.write('Mean of the hours  when groupby')
    with col2:
        st.write('Mean of the day when groupby')
    data = pd.read_csv(data_path)
    for param in data.columns[1:]:  
            home_page(st, data, param) 

elif selected_page == "Visualization":
    data = pd.read_csv(data_path, index_col='Date')
    if visualization_types == "Line":
        for param in data.columns:
            visualize_line_plot(st, data, param)
    elif visualization_types == "Scatter":
        for param in data.columns:
            visualize_scatter_plot(st, data, param)
    elif visualization_types == "Area Chart":
        for param in data.columns:
            visualize_area_chart(st, data, param)
    else:
        for param in data.columns:
            visualize_histogram_plot(st, data, param)

elif selected_page == "Forecasting":
    data = pd.read_csv(data_path, index_col='Date')
    if forecast_algorithms == "Prophet":
        data = pd.read_csv(data_path)
        for param in data.columns[1:]:
            prophet_forecast(st, data, param)
    elif  forecast_algorithms == "LSTM":
        for param in data.columns:
            lstm_forecast(st, data, param)
    else :
        for param in data.columns:
            arima_forecast(st, data, param)

elif selected_page == 'Anomaly Detection':
    if  anomaly_detetection_algorithms == "LSTM":
        lstm_anomaly_detection_page(st)
    elif  anomaly_detetection_algorithms == "PyCaret":
        pycaret_anomaly_detection_page(st)
    else :
        data = pd.read_csv(data_path)
        for param in data.columns[1:]:
            prophet_anomaly_detection_page(st, data, param)

else:
    if blogs == "About Time Series":
        st.title("About Time Series")
    elif blogs == "About Prophet":
        st.title("About Prophet")
    elif blogs == "About LSTM":
        st.title("About LSTM")
    else:
        st.title("About ARIMA")
