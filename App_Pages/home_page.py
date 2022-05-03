import pandas as pd
from plotly import graph_objs as go 

# DATASET_PATH = 'Dataset/'

data = pd.read_csv('Dataset/İstanbul/İstanbulAverageDF.csv')
total_column_names = data.columns
total_column_names = total_column_names[1:]

def home_page(st):
    st.title("""Air Quality of Turkey """)
    
    part_of_data = data.loc[data['Date'] < '2021-10-18']
    
    st.write(data.tail())
    st.write(part_of_data)
