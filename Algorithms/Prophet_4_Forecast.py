'''
data wil be loaded from dataset folder. then that data will be used for anomaly detection. After model training the model will be saved for app. On app side anoly will be detected over the saved model. Periodically saved model will be updated by new datas.
'''
'''
    Train anomaly detection for different all columns and visualize the columns base oon their own anomaly model.
''' 


"""
    * Forecasting types : 
        * General Forecasting Models (AR - MA - ARMA - ARIMA) 
        * Deep Learning for Forecasting
        # * Facebook's Prophet
"""

import streamlit as st 
from datetime import date
import yfinance as yf 
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go 

def prophet_for_forecast():
    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    stocks = ("AAPL", "MSFT", "GME")
    selected_stocks = st.selectbox("Select dataset for prediction", stocks)

    n_years = st.slider("Years of prediction:", 1, 4)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Load data ...")
    data = load_data(selected_stocks)
    data_load_state.text("Loading data .. Done!")

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()

    # Predict forecast with Prophet.
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
        
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)
