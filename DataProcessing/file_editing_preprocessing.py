# ************************* File System Editing ****************************

# ONE BY ONE
# 1) Read the data 
# 2) Convert data to dataframe (Dont forget DateTime fow index column)
# 3) Fill NaN values with mean value of the column
# 4) Convert all values between 0-1 
# 5) Concat the all files in one new df 
# 6) Use groubby method on the new df based on time values (Get mean of the variables)
# 7) Save new file as .csv filetype





from asyncore import read
import pandas as pd

# read_file = pd.read_excel(r'Data path that you want to convert.xlsx')
# read_file.to_csv(r'Converted data path should save.csv', index=None, header=True)

df = pd.DataFrame({'Time': ['03/06/2019 00:00:56','03/06/2019 00:00:56', '03/06/2019 01:00:56', '03/06/2019 01:00:56', '03/06/2019 02:00:56', '03/06/2019 03:00:56', '03/06/2019 04:00:56'], 'pm':[148.79, 100, 164.50, 90, 143.17, 127.49, 100.78], 'so':[47.63, 50.63, 42.96, 50.96,28.43, 18.94, 16.71]}, columns=['Time', 'pm', 'so'])

print(f'Old df is \n\n{df}\n\n')

# df.groupby('Time')
df = df.groupby("Time").sum()

print(df)


