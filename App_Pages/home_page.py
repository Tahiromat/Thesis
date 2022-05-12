import pandas as pd
import plotly.express as px
from plotly import graph_objs as go

def home_page(st, data):
    data['Date'] = pd.to_datetime(data['Date'])
    st.write(data.head())


def home_page_vis_help(st, data, selected_param):
    data = data.set_index('Date').resample('H').mean().reset_index()

    data['hour'] = data.Date.dt.hour
    data['weekday'] = pd.Categorical(data.Date.dt.strftime('%A'), categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)

    hourly_data_mean = data[[selected_param, 'hour']].groupby('hour').mean()
    weekly_data_mean = data[[selected_param, 'weekday']].groupby('weekday').mean()

    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Line(x=hourly_data_mean.index, y=data[selected_param]))
        fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=600)
        st.plotly_chart(fig)

    with col2:
        fig = go.Figure()
        fig.add_trace(go.Line(x=weekly_data_mean.index, y=data[selected_param]))
        fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=True, width=800, height=600)
        st.plotly_chart(fig)