import pandas as pd
import plotly.express as px

def home_page(st, data):
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.loc[data['Date'] >= '2022-03-01']
    st.title('Air Quality of Turkey')

    st.write('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
    
    st.markdown('#')
    # st.header('Where is Data Coming')
    # graphviz_4home(st)

    st.markdown('#')
    st.header('Some Graph to understand data')
    pie_chart_4home(st, data)



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
    fig.layout.update(width=900, height=600)
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