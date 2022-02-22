import streamlit as st
import pandas as pd

from App.runfilesbeforeappload import CallPy

# 
CallPy(path="webscrap.py").call_python_file()
st.write("""  #Hello Streamlit  """)


