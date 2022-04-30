import streamlit as st 
from datetime import date
import yfinance as yf 
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go 
import pandas as pd
import os

DATASET_PATH = 'Dataset/'

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')

cities = []
stations = []



def home_page():
    st.title("""Air Quality of Turkey """)
    
    find_data()
    


# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def find_data():
    cities.clear()
    selected_city = st.selectbox('Select City', choose_city(DATASET_PATH))
    # st.write(selected_city)

    stations.clear()
    selected_station = st.selectbox('Select Station', choose_station(DATASET_PATH, selected_city))
    # st.write(selected_station)

    data_path = f"{DATASET_PATH}{selected_city}/{selected_station}"
    st.write(data_path)

    data = pd.read_csv(data_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d %H:%M:%S.%f')

    st.write(data.head())


def choose_city(DATASET_PATH):
    for city in os.listdir(DATASET_PATH):
        cities.append(city)
        cities.sort()
    return cities
    

def choose_station(DATASET_PATH, selected_city):
    for station in os.listdir(DATASET_PATH + selected_city + '/'):
        stations.append(station)
        stations.sort()
    return stations
    

# NOTE:
    # Find dataset based on the choises. Choosing wil be on slider side