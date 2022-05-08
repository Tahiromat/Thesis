import numpy as np
import pandas as pd
from prophet import Prophet
import plotly.express as px

def lstm_anomaly_detection_page(st):
    st.write("LSTM algorithm has been choosed for anomaly detection")

def pycaret_anomaly_detection_page(st):
    st.write("PyCaret algorithm has been choosed for anomaly detection")

def prophet_anomaly_detection_page(st, df, selected_param):
    df = df[['Date', selected_param]]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').resample('H').mean().reset_index()
    #express to plot entire data
    # fig = px.line(df.reset_index(), x='Date', y=selected_param, title='XXAAXX')
    # #slider
    # fig.update_xaxes(
    #     rangeslider_visible = True,
    #     rangeselector = dict(
    #         buttons = list([
    #             dict(count=1, label='1y', step="year", stepmode="backward"),
    #             dict(count=2, label='2y', step="year", stepmode="backward"),
    #             dict(count=2, label='5y', step="year", stepmode="backward")
    #         ])
    #     )
    # )
    # fig.show()
    data = df.reset_index()[['Date', selected_param]].rename({'Date':'ds', selected_param:'y'}, axis='columns')
    train = data[(data['ds'] >= '2021-08-01') & (data['ds'] <= '2022-01-01')]
    test = data[(data['ds'] > '2022-01-01')]
    m = Prophet(changepoint_range=0.95)
    m.fit(train)
    future = m.make_future_dataframe(periods=119, freq='H')
    forecast = m.predict(future)
    print(forecast[['ds','yhat','yhat_lower','yhat_upper']].tail())
    result = pd.concat([data.set_index('ds')['y'], forecast.set_index('ds')[['yhat','yhat_lower','yhat_upper']]], axis=1)
    fig1 = m.plot(forecast)
    # plt.show()
    comp = m.plot_components(forecast)
    # plt.show()
    result['error'] = result['y'] - result['yhat']
    result['uncertainty'] = result['yhat_upper'] - result['yhat_lower']
    result['anomaly'] = result.apply(lambda x: 'Yes' if(np.abs(x['error']) > 1.5*x['uncertainty']) else 'No', axis = 1)
    #result['anomaly'] = np.where(np.abs(x['error']) > 1.5*x['uncertainty']), 'Yes', 'No') #Alternate way
    #visualize the anomaly data
    fig = px.scatter(result.reset_index(), x='ds', y='y', color='anomaly', title=selected_param)
    #slider
    fig.update_xaxes(
        rangeslider_visible = True,
        rangeselector = dict(
            buttons = list([
                dict(count=1, label='1y', step="year", stepmode="backward"),
                dict(count=2, label='3y', step="year", stepmode="backward"),
                dict(count=2, label='5y', step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    st.plotly_chart(fig)
