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

for city in os.listdir(DATASET_PATH):
    cities.append(city)
    cities.sort()

def home_page():
    st.title("""Air Quality of Turkey """)

    selected_city = st.selectbox('Select City', cities)
    
    st.write(selected_city)


    for station in os.listdir(DATASET_PATH + selected_city):
        stations.append(station)
        stations.sort()

    selected_station = st.selectbox('Select Station', stations)
    st.write(selected_station)
    stations.clear()
    # station_path = DATASET_PATH + selected_city + '/' + selected_station

    # st.write(station_path)
    # stations.clear()

           


def find_stations_based_on_cityname():
    pass
    
    



# NOTE :
    #  When you choose the city then stations need to be created based on that route 
    # And of the chosing a route need to be created for that specifik choosing