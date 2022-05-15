import numpy as np
import pandas as pd
from prophet import Prophet
import plotly.express as px
from sklearn.ensemble import IsolationForest

def lstm_anomaly_detection_page(st):
    st.write("LSTM algorithm has been choosed for anomaly detection")

def isolationforest_anomaly_detection_page(st, data, selected_param):
    df = data[['Date', selected_param]]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'] > '2021-06-01')]
    df = df.set_index('Date').resample('D').mean().reset_index()
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.scatter(df.reset_index(), x='Date', y=selected_param)
        fig1.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=500)
        st.plotly_chart(fig1)
    model = IsolationForest(contamination=0.004)
    model.fit(df[[selected_param]])
    df['outliers'] = pd.Series(model.predict(df[[selected_param]])).apply(lambda x: 'yes' if (x == -1) else 'no')
    with col2:
        fig2 = px.scatter(df.reset_index(), x='Date', y=selected_param, color='outliers')
        fig2.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=500)
        st.plotly_chart(fig2)

def prophet_anomaly_detection_page(st, data, selected_param):
    df = data[['Date', selected_param]]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').resample('D').mean().reset_index()
    df = df[(df['Date'] >= '2021-06-01')]
    data = df.reset_index()[['Date', selected_param]].rename({'Date':'ds', selected_param:'y'}, axis='columns')
    train = data[(data['ds'] >= '2021-06-01') & (data['ds'] <= '2022-02-01')]
    test = data[(data['ds'] > '2022-02-01')]
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.scatter(df.reset_index(), x='Date', y=selected_param)
        fig1.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=500)
        st.plotly_chart(fig1)
    m = Prophet(changepoint_range=0.95)
    m.fit(train)
    future = m.make_future_dataframe(periods=30, freq='D')
    forecast = m.predict(future)
    result = pd.concat([data.set_index('ds')['y'], forecast.set_index('ds')[['yhat','yhat_lower','yhat_upper']]], axis=1)
    # fig2 = m.plot(forecast)
    result['error'] = result['y'] - result['yhat']
    result['uncertainty'] = result['yhat_upper'] - result['yhat_lower']
    result['anomaly'] = result.apply(lambda x: 'Yes' if(np.abs(x['error']) > 1.5*x['uncertainty']) else 'No', axis = 1)
    with col2:
        fig2 = px.scatter(result.reset_index(), x='ds', y='y', color='anomaly')
        fig2.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=500)
        st.plotly_chart(fig2)

