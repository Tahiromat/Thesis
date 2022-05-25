import numpy as np
import pandas as pd
import pydeck as pdk
import plotly.express as px
from plotly import graph_objs as go

def home_page(st, data):
    data['Date'] = pd.to_datetime(data['Date'])
    # data = data.loc[data['Date'] >= '2022-03-01']
    st.title('Air Quality Analysis of Turkey')

    # map_view(st, 41.015137, 28.979530) # Istanbul
    # map_view(st, 41.637602, 32.333811) 
    st.markdown('#')
    pie_chart_4home(st, data)
    st.markdown('#')
    col1, col2 = st.columns(2)
    with col1:
        bar_chart_4home(st, data)
    with col2:
        line_chart_4home(st, data)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! HOME PAGE HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def map_view(st, lat, lon):
    # df = pd.DataFrame(
    # np.random.randn(100, 2) / [25, 25] + [lat, long],
    # columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=11,
            pitch=50,
        ),
        layers=[
            # pdk.Layer(
            #     'HexagonLayer',
            #     # data=df,
            #     get_position='[lon, lat]',
            #     radius=200,
            #     elevation_scale=4,
            #     elevation_range=[0, 1000],
            #     pickable=True,
            #     extruded=True,
            # ),
            pdk.Layer(
                'ScatterplotLayer',
                # data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

def pie_chart_4home(st, data):
    mean_values = []
    for i in data.columns[1:]:
        data_m = data[i].mean()
        mean_values.append(data_m)
    df_mean = pd.DataFrame()
    df_mean['Names'] = data.columns[1:]
    df_mean['Values'] = mean_values
    col1, col2 = st.columns(2)
    fig = px.pie(df_mean, values='Values', names='Names')
    fig.layout.update(width=1500, height=600)
    st.plotly_chart(fig)

def bar_chart_4home(st, data):
    for i in data.columns[1:]:
        data = data.set_index('Date').resample('D').mean().reset_index()
        data['year'] = data.Date.dt.year
        yearly_data_mean = data[[i, 'year']].groupby('year').mean()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=yearly_data_mean.index, y=yearly_data_mean[i]))
        fig.layout.update(title_text=i, xaxis_rangeslider_visible=False, width=800, height=600)    
        st.plotly_chart(fig)
    
def line_chart_4home(st, data):
    for i in data.columns[1:]:
        data = data.set_index('Date').resample('D').mean().reset_index()
        data['year'] = data.Date.dt.year
        yearly_data_mean = data[[i, 'year']].groupby('year').mean()
        fig = go.Figure()
        fig.add_trace(go.Line(x=yearly_data_mean.index, y=yearly_data_mean[i]))
        fig.layout.update(title_text=i, xaxis_rangeslider_visible=False, width=800, height=600)    
        st.plotly_chart(fig)

def graphviz_4home(st):
    st.graphviz_chart('''
    digraph {
        TurkeyAIRQUALITYDATABANK  -> StationsData
        StationsData  -> UniqCityFolder
        UniqCityFolder -> Dataset
        Dataset -> Home
        Dataset -> Visualization
        Dataset -> Analysis
        Dataset -> AnomalyDetection
        Dataset -> Forecasting
        }
    ''')

