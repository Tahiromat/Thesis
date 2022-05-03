from tkinter import Y
import matplotlib
from matplotlib.pyplot import grid
import pandas as pd
import streamlit as st
import numpy as np

from plotly import graph_objs as go
import plotly.express as px

from App_Pages.generate_data_basedon_selections import find_data

# DATASET_PATH = 'Dataset/'

# data = find_data(DATASET_PATH)
# total_column_names = data.columns
# total_column_names = total_column_names[1:]

data = pd.read_csv('Dataset/İstanbul/İstanbulAverageDF.csv')
total_column_names = data.columns
total_column_names = total_column_names[1:]

def line_visualization_page():
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)
    visualize_line_plot(selected_param)

def scatter_visualization_page():
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)
    visualize_scatter_plot(selected_param)

def histogram_visualization_page():
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)
    visualize_histogram_plot(selected_param)

# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def visualize_line_plot(y_axis):
    fig = go.Figure()
    fig.add_trace(go.Line(x=data['Date'], y=data[y_axis]))
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def visualize_scatter_plot(y_axis):
    fig = go.Figure(data=[go.Scatter(x=data['Date'], y=data[y_axis], mode = "markers")])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def visualize_histogram_plot(y_axis):
    fig = px.histogram(data, x=data[y_axis])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)