from tkinter import Y
import matplotlib
from matplotlib.pyplot import grid
import pandas as pd
import streamlit as st

from plotly import graph_objs as go


df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')


def line_visualization_page():
    st.title("Visualization Page")

    def visualize_PM10():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['PM10 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='PM10 ( µg/m3 )', xaxis_rangeslider_visible=True)

        st.plotly_chart(fig)

    visualize_PM10()


    def visualize_PM_25():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['PM 2.5 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='PM 2.5 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_PM_25()


def scatter_visualization_page():
    st.write("Visualization type is scatter")