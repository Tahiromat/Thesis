from tkinter import Y
import matplotlib
from matplotlib.pyplot import grid
import pandas as pd
import streamlit as st
import numpy as np

from plotly import graph_objs as go
# import plotly.graph_objects as px
import plotly.express as px

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')

def line_visualization_page():
    st.title("Line Visualization")
    visualize_line_plot('PM10 ( µg/m3 )')
    visualize_line_plot('PM 2.5 ( µg/m3 )')
    visualize_line_plot('SO2 ( µg/m3 )')
    visualize_line_plot('CO ( µg/m3 )')
    visualize_line_plot('NO2 ( µg/m3 )')
    visualize_line_plot('NOX ( µg/m3 )')
    visualize_line_plot('O3 ( µg/m3 )')

def scatter_visualization_page():
    st.title("Scatter Visualization")
    visualize_scatter_plot('PM10 ( µg/m3 )')
    visualize_scatter_plot('PM 2.5 ( µg/m3 )')
    visualize_scatter_plot('SO2 ( µg/m3 )')
    visualize_scatter_plot('CO ( µg/m3 )')
    visualize_scatter_plot('NO2 ( µg/m3 )')
    visualize_scatter_plot('NOX ( µg/m3 )')
    visualize_scatter_plot('O3 ( µg/m3 )')

def histogram_visualization_page():
    st.title("Histogram Visualization")
    visualize_histogram_plot('PM10 ( µg/m3 )')
    visualize_histogram_plot('PM 2.5 ( µg/m3 )')
    visualize_histogram_plot('SO2 ( µg/m3 )')
    visualize_histogram_plot('CO ( µg/m3 )')
    visualize_histogram_plot('NO2 ( µg/m3 )')
    visualize_histogram_plot('NOX ( µg/m3 )')
    visualize_histogram_plot('O3 ( µg/m3 )')


# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!

def visualize_line_plot(y_axis):
    fig = go.Figure()
    fig.add_trace(go.Line(x=df['Date'], y=df[y_axis]))
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def visualize_scatter_plot(y_axis):
    fig = go.Figure(data=[go.Scatter(x=df['Date'], y=df[y_axis], mode = "markers")])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


def visualize_histogram_plot(y_axis):
    fig = px.histogram(df, x=df['PM10 ( µg/m3 )'])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)