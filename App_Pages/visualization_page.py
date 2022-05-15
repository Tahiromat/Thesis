import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from plotly import graph_objs as go

def visualize_line_plot(st, data, y_axis):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2022-03-01']
    data = data.resample('D').mean()
    fig = go.Figure()
    fig.add_trace(go.Line(x=data.index, y=data[y_axis]))
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def visualize_scatter_plot(st, data, y_axis):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2022-03-01']
    data = data.resample('D').mean()
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data[y_axis], mode = "markers")])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)

def visualize_area_chart(st, data, y_axis):
    data = data[y_axis]
    data = data.loc[data.index >= '2022-03-01']
    st.markdown("#")
    st.markdown("#")
    st.area_chart(data)

def visualize_histogram_plot(st, data, y_axis):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2020-03-01']
    data = data.resample('D').mean()

    hist_data = [data[y_axis]]
    group_labels = [y_axis]
    fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=False, width=1500, height=600)
    st.plotly_chart(fig)
