import math
import numpy as np
import pandas as pd
from prophet import Prophet
import statsmodels.api as smapi
from plotly import graph_objs as go
from prophet.plot import plot_plotly
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, LSTM

def prophet_forecast(st, data, forecast_column_name):
    n_years = 1
    period = n_years * 10
    data = data.loc[data['Date'] >= '2022-03-01']
    data['Date'] = pd.to_datetime(data['Date'])
    data.reset_index(drop=True, inplace=True)
    df_train = data[['Date', forecast_column_name]]     
    df_train = df_train.rename(columns={"Date": "ds", forecast_column_name: "y"})
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(period)
    forecast = m.predict(future)
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

def lstm_forecast(st, data, forecast_parameter):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2021-01-01']
    data = data.resample('D').mean()
    data = data.filter([forecast_parameter])
    dataset = data.values
    training_data_len = math.ceil(len(dataset) * .8)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    train_data = scaled_data[0:training_data_len, :]
    x_train = []
    y_train = []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=128, epochs=2)
    test_data = scaled_data[training_data_len - 60 : , :]
    x_test = []
    y_test = dataset[training_data_len : , :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60 : i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    rms = np.sqrt(np.mean(predictions - y_test)**2)
    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions
    fig = go.Figure()
    fig.add_trace(go.Line(x=train.index, y=train[forecast_parameter]))
    fig.add_trace(go.Line(x=valid.index, y=valid[forecast_parameter]))
    fig.add_trace(go.Line(x=valid.index, y=valid['Predictions']))
    fig.layout.update(title_text=forecast_parameter, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)
    
def arima_forecast(st, data, forecasted_param):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2020-01-01']
    data = data.resample('D').mean()
    df = data[[forecasted_param]].copy()
    n = int(len(df) * 0.8)
    train = df[forecasted_param][:n]
    test = df[forecasted_param][n:]
    model = smapi.tsa.arima.ARIMA(train, order=(6, 1, 3))
    # model = ARIMA(train, order=(6, 1, 3))
    result = model.fit()
    step = 30
    fc = result.forecast(step, alpha=0.01)
    # fc, se, conf = result.forecast(step, alpha=0.05)
    fc = pd.Series(fc, index=test[:step].index)
    # lower = pd.Series(conf[:, 0], index=test[:step].index)
    # upper = pd.Series(conf[:, 1], index=test[:step].index)
    fig = go.Figure()
    fig.add_trace(go.Line(x=df.index, y=df[forecasted_param]))
    fig.add_trace(go.Line(x=test.index, y=test[:step]))
    fig.add_trace(go.Line(x=fc.index, y = fc))
    # fig.add_trace(go.Line(x=valid.index, y=valid['Predictions']))
    fig.layout.update(title_text=forecasted_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)