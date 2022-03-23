# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# iki aynı isme sahip data sette zaman aralığı farklı olduğunda concat birleştirme nasıl bir çıktı veriyor incele

import pandas as pd


df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Aydın/Aydın.csv')

print(df.info())

print('\n\n')

print(df)