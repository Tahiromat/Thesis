import pandas as pd
import plotly.express as px
from plotly import graph_objs as go

def hourly_analysis(st, data, selected_param):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date').resample('H').mean().reset_index()
    data['hour'] = data.Date.dt.hour
    hourly_data_mean = data[[selected_param, 'hour']].groupby('hour').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=hourly_data_mean.index, y=data[selected_param]))
    fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def daily_analysis(st, data, selected_param):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date').resample('H').mean().reset_index()
    data['daysofmonth'] = data.Date.dt.day
    daily_data_mean = data[[selected_param, 'daysofmonth']].groupby('daysofmonth').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=daily_data_mean.index, y=data[selected_param]))
    fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def weekly_analysis(st, data, selected_param):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date').resample('H').mean().reset_index()
    data['daysofweek'] = pd.Categorical(data.Date.dt.weekday, categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)
    weekly_data_mean = data[[selected_param, 'daysofweek']].groupby('daysofweek').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=weekly_data_mean.index, y=data[selected_param]))
    fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def monthly_analysis(st, data, selected_param):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date').resample('H').mean().reset_index()
    data['monthsofyear'] = pd.Categorical(data.Date.dt.month, categories=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"], ordered=True)
    monthly_data_mean = data[[selected_param, 'monthsofyear']].groupby('monthsofyear').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=monthly_data_mean.index, y=data[selected_param]))
    fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def yearly_analysis(st, data, selected_param):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.set_index('Date').resample('H').mean().reset_index()
    data['year'] = data.Date.dt.year
    yearly_data_mean = data[[selected_param, 'year']].groupby('year').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=yearly_data_mean.index, y=data[selected_param]))
    fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)