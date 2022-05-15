import pandas as pd
import plotly.express as px


def home_page(st, data):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.loc[data['Date'] >= '2022-03-01']
    st.write(data.head())


    mean_values = []
    for i in data.columns[1:]:
        data_m = data[i].mean()
        mean_values.append(data_m)
    df_mean = pd.DataFrame()
    df_mean['Names'] = data.columns[1:]
    df_mean['Values'] = mean_values
    fig = px.pie(df_mean, values='Values', names='Names')
    fig.layout.update(xaxis_rangeslider_visible=False, width=1500, height=600)
    st.plotly_chart(fig)



