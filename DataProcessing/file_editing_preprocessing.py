# ************************* File System Editing ****************************

# ONE BY ONE
#  Read the data 
#  Convert data to dataframe (Dont forget DateTime fow index column)
#  Fill NaN values with mean value of the column
#  Convert all values between 0-1 
#  Concat the all files in one new df 
#  Use groubby method on the new df based on time values (Get mean of the variables)
#  Save new file as .csv filetype


# Write a function that open all files and convert them into csv file.


from asyncore import read
from math import fabs
from turtle import shape
import pandas as pd
import glob


'''
data1 = pd.read_excel(r'RawData/Kocaeli/alikahyamthm.xlsx')
data1.to_csv(r'RawData/Kocaeli/alikahyamthm.csv', index=None, header=True)

data2 = pd.read_excel(r'RawData/Kocaeli/altınovamthm.xlsx')
data2.to_csv(r'RawData/Kocaeli/altınovamthm.csv', index=None, header=True)

data3 = pd.read_excel(r'RawData/Kocaeli/dilovası.xlsx')
data3.to_csv(r'RawData/Kocaeli/dilovası.csv', index=None, header=True)

data4 = pd.read_excel(r'RawData/Kocaeli/dilovasıimesosb1mthm.xlsx')
data4.to_csv(r'RawData/Kocaeli/dilovasıimesosb1mthm.csv', index=None, header=True)

data5 = pd.read_excel(r'RawData/Kocaeli/dilovasıimesosb2mthm.xlsx')
data5.to_csv(r'RawData/Kocaeli/dilovasıimesosb2mthm.csv', index=None, header=True)

data6 = pd.read_excel(r'RawData/Kocaeli/gebzemthm.xlsx')
data6.to_csv(r'RawData/Kocaeli/gebzemthm.csv', index=None, header=True)

data7 = pd.read_excel(r'RawData/Kocaeli/gebzeosbmthm.xlsx')
data7.to_csv(r'RawData/Kocaeli/gebzeosbmthm.csv', index=None, header=True)

data8 = pd.read_excel(r'RawData/Kocaeli/gölcükmthm.xlsx')
data8.to_csv(r'RawData/Kocaeli/gölcükmthm.csv', index=None, header=True)

data9 = pd.read_excel(r'RawData/Kocaeli/izmitmthm.xlsx')
data9.to_csv(r'RawData/Kocaeli/izmitmthm.csv', index=None, header=True)

data10 = pd.read_excel(r'RawData/Kocaeli/kandıramthm.xlsx')
data10.to_csv(r'RawData/Kocaeli/kandıramthm.csv', index=None, header=True)

data11 = pd.read_excel(r'RawData/Kocaeli/kocaeli.xlsx')
data11.to_csv(r'RawData/Kocaeli/kocaeli.csv', index=None, header=True)

data12 = pd.read_excel(r'RawData/Kocaeli/korfezmthm.xlsx')
data12.to_csv(r'RawData/Kocaeli/korfezmthm.csv', index=None, header=True)

data13 = pd.read_excel(r'RawData/Kocaeli/yeniköymthm.xlsx')
data13.to_csv(r'RawData/Kocaeli/yeniköymthm.csv', index=None, header=True)

'''

data1 = pd.read_csv('RawData/Kocaeli/alikahyamthm.csv')
data2 = pd.read_csv('RawData/Kocaeli/altınovamthm.csv')
data3 = pd.read_csv('RawData/Kocaeli/dilovası.csv')
data4 = pd.read_csv('RawData/Kocaeli/dilovasıimesosb1mthm.csv')
data5 = pd.read_csv('RawData/Kocaeli/dilovasıimesosb2mthm.csv')
data6 = pd.read_csv('RawData/Kocaeli/gebzemthm.csv')
data7 = pd.read_csv('RawData/Kocaeli/gebzeosbmthm.csv')
data8 = pd.read_csv('RawData/Kocaeli/gölcükmthm.csv')
data9 = pd.read_csv('RawData/Kocaeli/izmitmthm.csv')
data10 = pd.read_csv('RawData/Kocaeli/kandıramthm.csv')
data11 = pd.read_csv('RawData/Kocaeli/kocaeli.csv')
data12 = pd.read_csv('RawData/Kocaeli/korfezmthm.csv')
data13 = pd.read_csv('RawData/Kocaeli/yeniköymthm.csv')


DF = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13], ignore_index=False)


DF.groupby('Tarih')
DF = DF.groupby('Tarih').mean()
print(DF)

# DF.to_csv('Dataset/Kocaeli/newdf.csv')
# df = pd.DataFrame({'Time': ['03/06/2019 00:00:56','03/06/2019 00:00:56', '03/06/2019 01:00:56', '03/06/2019 01:00:56', '03/06/2019 02:00:56', '03/06/2019 03:00:56', '03/06/2019 04:00:56'], 'pm':[148.79, 100, 164.50, 90, 143.17, 127.49, 100.78], 'so':[47.63, 50.63, 42.96, 50.96,28.43, 18.94, 16.71]}, columns=['Time', 'pm', 'so'])

# print(f'Old df is \n\n{df}\n\n')

# # df.groupby('Time')
# df = df.groupby("Time").sum()

# print(df)


