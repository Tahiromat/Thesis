def home_page(st, data):

    st.markdown('#')

    st.markdown('Data Columns')
    st.write(data.columns)

    st.markdown('#')

    st.markdown('Head of data')
    st.write(data)

