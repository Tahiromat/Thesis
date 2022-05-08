import streamlit as st 
import pandas as pd
import os

cities = []
stations = []

def find_data(st, DATASET_PATH):
    cities.clear()
    selected_city = st.selectbox('Select City', choose_city(DATASET_PATH))
    st.markdown("###")  
    stations.clear()
    selected_station = st.selectbox('Select Station', choose_station(DATASET_PATH, selected_city))
    data_path = f"{DATASET_PATH}{selected_city}/{selected_station}"
    return data_path

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