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

    data = pd.read_csv(data_path)
    data = data.loc[data['Date'] >= '2022-03-01']
    
    data['Date'] = pd.to_datetime(data['Date'])
    data.reset_index(drop=True, inplace=True)
    
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


# DATASET_PATH = 'Dataset/'

# data = find_data(DATASET_PATH)
# total_column_names = data.columns
# total_column_names = total_column_names[1:]




#  data = pd.read_csv(data_path, index_col=False)
    
#     data['Date'] = pd.to_datetime(data['Date'])
#     data = data.set_index(data['Date'])
#     data = data.resample('D').mean()
