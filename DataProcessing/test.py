import pandas as pd



df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Mersin/mersin1.csv')
df['Tarih'] = pd.to_datetime(df['Tarih'])
print(df.info())