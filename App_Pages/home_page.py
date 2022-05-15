import pandas as pd

def home_page(st, data):
    data['Date'] = pd.to_datetime(data['Date'])
    
    st.write(data.head())


