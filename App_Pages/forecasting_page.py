from fbprophet import Prophet
from fbprophet.plot import plot_plotly

# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def prophet_forecast(st, data, forecast_column_name):

    n_years = 1
    period = n_years * 10

    df_train = data[['Date', forecast_column_name]]     
    df_train = df_train.rename(columns={"Date": "ds", forecast_column_name: "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)


def lstm_forecast(st):
    st.title("LSTM Forecasting")
    pass


def arima_forecast(st):
    st.title("ARIMA Forecasting")
    pass

