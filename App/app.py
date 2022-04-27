from tkinter import Y
import matplotlib
from matplotlib.pyplot import grid
import pandas as pd
import streamlit as st
# import fbprophet import Prophet
# from pbprophet.plot import Prophet
from plotly import graph_objs as go
from streamlit_option_menu import option_menu
from streamlit_page_helper_methods import city_names



MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
CITY_NAMES_FOR_SIDE_BAR = city_names(MAIN_FOLDER_PATH)

st.sidebar.selectbox('Cities', CITY_NAMES_FOR_SIDE_BAR)


# From here you will choose data set 
df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Horizontal Menu
selected = option_menu(None, ["Home", "Visualization", "Forecasting", 'Anomaly D.', 'Choose City'], 
    icons=['house', 'cloud-upload', "list-task", 'gear', 'list'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == "Home":

    st.write("""### Anomaly Detection in Air Quality of Turkey """)
    st.markdown(""" ### """)
    st.markdown(""" ### """)
    def visualize_PM10():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['PM10 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='PM10 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
        
    visualize_PM10()


if selected == "Visualization":
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


    def visualize_SO2():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['SO2 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='SO2 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_SO2()


    def visualize_CO():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['CO ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='CO ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_CO()


    def visualize_NO2():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['NO2 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='NO2 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_NO2()


    def visualize_NOX():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['NOX ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='NOX ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_NOX()


    def visualize_O3():
        fig =go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['O3 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='O3 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_O3()

if selected == "Forecasting":
    def visualize_PM10():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['PM10 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='PM10 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_PM10()


if selected == "Anomaly D.":
    def visualize_PM10():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['PM10 ( µg/m3 )']))
        fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.layout.update(title_text='PM10 ( µg/m3 )', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    visualize_PM10()



