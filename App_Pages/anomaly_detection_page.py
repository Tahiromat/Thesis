import numpy as np
import pandas as pd
from prophet import Prophet
import plotly.express as px

def lstm_anomaly_detection_page(st):
    st.write("LSTM algorithm has been choosed for anomaly detection")

def pycaret_anomaly_detection_page(st):
    st.write("PyCaret algorithm has been choosed for anomaly detection")

def prophet_anomaly_detection_page(st, data, selected_param):
    df = data[['Date', selected_param]]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').resample('H').mean().reset_index()
    df = df[(df['Date'] > '2021-12-30')]
    data = df.reset_index()[['Date', selected_param]].rename({'Date':'ds', selected_param:'y'}, axis='columns')
    train = data[(data['ds'] >= '2022-01-01') & (data['ds'] <= '2022-02-01')]
    test = data[(data['ds'] > '2022-03-01')]
    col1, col2 = st.columns(2)
    fig1 = px.line(df.reset_index(), x='Date', y=selected_param)
    fig1.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=600)
    with col1:
        st.plotly_chart(fig1)
    m = Prophet(changepoint_range=0.95)
    m.fit(train)
    future = m.make_future_dataframe(periods=119, freq='H')
    forecast = m.predict(future)
    result = pd.concat([data.set_index('ds')['y'], forecast.set_index('ds')[['yhat','yhat_lower','yhat_upper']]], axis=1)
    fig1 = m.plot(forecast)
    result['error'] = result['y'] - result['yhat']
    result['uncertainty'] = result['yhat_upper'] - result['yhat_lower']
    result['anomaly'] = result.apply(lambda x: 'Yes' if(np.abs(x['error']) > 1.5*x['uncertainty']) else 'No', axis = 1)
    fig2 = px.scatter(result.reset_index(), x='ds', y='y', color='anomaly')
    fig2.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=600)
    with col2:
        st.plotly_chart(fig2)
    