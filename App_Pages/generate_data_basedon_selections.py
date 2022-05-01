import streamlit as st 
import pandas as pd
import os

# DATASET_PATH = 'Dataset/'

cities = []
stations = []

def find_data(DATASET_PATH):
    cities.clear()
    selected_city = st.selectbox('Select City', choose_city(DATASET_PATH))

    stations.clear()
    selected_station = st.selectbox('Select Station', choose_station(DATASET_PATH, selected_city))

    data_path = f"{DATASET_PATH}{selected_city}/{selected_station}"

    data = pd.read_csv(data_path)
    data['Date'] = pd.to_datetime( data['Date'])

    return data


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
