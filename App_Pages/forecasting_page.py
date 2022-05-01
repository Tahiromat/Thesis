import streamlit as st
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from App_Pages.generate_data_basedon_selections import find_data

DATASET_PATH = 'Dataset/'

data = find_data(DATASET_PATH)
total_column_names = data.columns
total_column_names = total_column_names[1:]

def prophet_forecasting_page():
    st.title("Prophet Forecasting")
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)

    prophet_forecast(selected_param)


def lstm_forecasting_page():
    st.title("LSTM Forecasting")
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)
    lstm_forecast(selected_param)


def arima_forecasting_page():
    st.title("ARIMA Forecasting")
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)
    arima_forecast(selected_param)


def autoencoder_forecasting_page():
    st.title("AUTOENCODER Forecasting")
    selected_param = st.selectbox("Select Parameter you want to visualize", total_column_names)

    autoencoder_forecast(selected_param)


# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def prophet_forecast(forecast_column_name):
    n_years = st.slider("Years of prediction:", 1, 3)
    period = n_years * 365

    df_train = data[['Date',forecast_column_name]]
    df_train = df_train.rename(columns={"Date": "ds", forecast_column_name: "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)


def lstm_forecast(forecast_column_name):
    pass


def arima_forecast(forecast_column_name):
    pass


def autoencoder_forecast(forecast_column_name):
    pass
