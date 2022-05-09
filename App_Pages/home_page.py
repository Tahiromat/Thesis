import pandas as pd

def home_page(st, data):
    data.index = pd.to_datetime(data.index)
    data = data.loc[data.index >= '2022-03-20']
    data = data.resample('D').mean()
    st.markdown('#')
    st.markdown('#')
    st.markdown('Head of data')
    st.write(data)
    st.markdown('#')
    st.markdown('#')
    st.area_chart(data)
    st.markdown('#')
    st.line_chart(data)
    



