import streamlit as st 
from datetime import date
import yfinance as yf 
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go 
import pandas as pd

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')


def home_page():
    st.title("""Air Quality of Turkey """)
    st.write(df.head())
    