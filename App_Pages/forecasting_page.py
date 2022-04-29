import streamlit as st
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
# df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')


def prophet_forecasting_page():
    st.title("Prophet Forecasting")
    
    params = df.columns[1:]
    selected_param = st.selectbox('Select aparameter to forecast', params)

    prophet_forecast(selected_param)


def lstm_forecasting_page():
    st.title("LSTM Forecasting")
    
    params = df.columns[1:]
    selected_param = st.selectbox('Select aparameter to forecast', params)

    lstm_forecast(selected_param)


def arima_forecasting_page():
    st.title("ARIMA Forecasting")
    
    params = df.columns[1:]
    selected_param = st.selectbox('Select aparameter to forecast', params)

    arima_forecast(selected_param)


def autoencoder_forecasting_page():
    st.title("AUTOENCODER Forecasting")
    
    params = df.columns[1:]
    selected_param = st.selectbox('Select aparameter to forecast', params)

    autoencoder_forecast(selected_param)


# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def prophet_forecast(forecast_column_name):
    n_years = st.slider("Years of prediction:", 1, 3)
    period = n_years * 365

    df_train = df[['Date',forecast_column_name]]
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
