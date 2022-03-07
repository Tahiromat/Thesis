import pandas as pd

def read_excel_file(raw_path, raw_name):
    return pd.read_excel(f'{raw_path}/{raw_name}.xlsx')


def convert_xlsx2csv(df, path, save_name):
    df.to_csv(f'{path}/{save_name}.csv', index=None, header=True)
