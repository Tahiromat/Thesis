import plotly.express as px
from plotly import graph_objs as go

# !!!!!!!!!!!!!!!!!!!!!!! HELPER METHODS !!!!!!!!!!!!!!!!!!!!!!!


def visualize_line_plot(st, data, y_axis):
    fig = go.Figure()
    fig.add_trace(go.Line(x=data.index, y=data[y_axis]))
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)


def visualize_scatter_plot(st, data, y_axis):
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data[y_axis], mode = "markers")])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)


def visualize_histogram_plot(st, data, y_axis):
    fig = px.histogram(data, x=data[y_axis])
    fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=True, width=1500, height=600)
    st.plotly_chart(fig)