# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# iki aynı isme sahip data sette zaman aralığı farklı olduğunda concat birleştirme nasıl bir çıktı veriyor incele

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Adana/AdanaAverageDF.csv')
df['Date'] = pd.to_datetime(df['Date'])
print('\n\n')
print(df.info())
print('\n\n')
print(df.head())
print('\n\n')
