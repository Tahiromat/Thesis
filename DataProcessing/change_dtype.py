
def change_dtype_utility(df, name, current_param, replaced_param):
    
    return df[name].astype(str).str.replace(current_param,replaced_param)
