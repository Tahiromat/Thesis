# There will be file type changing from .xlsx to .csv 


from asyncore import read
import pandas as pd

read_file = pd.read_excel(r'Data path that you want to convert.xlsx')
read_file.to_csv(r'Converted data path should save.csv', index=None, header=True)
