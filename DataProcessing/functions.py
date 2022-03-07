from fileinput import filename
import pandas as pd
import os
from  read_and_convert_file import convert_xlsx2csv, read_excel_file

PATH = 'RawData/Kocaeli'
os.chdir(PATH)

raw_path = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData/Kocaeli'
save_path = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/DataProcessing'
raw_name = 'alikahyamthm'
save_name = 'alikahyamthm'

convert_xlsx2csv(read_excel_file(raw_path, raw_name), save_path, save_name)


# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)
#     if f_ext=='.xlsx':
#         print(f_name)
#         print(f_ext)
        # f = pd.read_excel(r'$PATH/f_name.xlsx')
        # f.to_csv(r'$PATH/f_name'.csv, index=None, header=True)


#     # # print(f_name)

#     # f = pd.read_excel(r'$PATH/f_name.xlsx')
#     # f.to_csv(r'PATH/f_name'.csv, index=None, header=True)

    