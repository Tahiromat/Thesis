from hashlib import new
from operator import le
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# iki aynı isme sahip data sette zaman aralığı farklı olduğunda concat birleştirme nasıl bir çıktı veriyor incele

df = pd.read_excel('/home/tahir/Downloads/Veri Detayları3_20_2022, 3_18_25 PM.xlsx')
file_name = df.columns[1]

# df = df.drop(df[:1])
# df = df.drop(labels=0, axis=0)
first2_row = df.loc[1]

print(first2_row)
print(file_name)