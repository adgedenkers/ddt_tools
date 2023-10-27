


import pandas as pd

def clean_dataframe(df):
    # create a new dataframe to store the cleaned data
    cleaned_df = pd.DataFrame()

    # loop through each row and column
    for col in df.columns:
        # cleaned df column = (if float, convert to int, then convert everything to string except nulls)
        cleaned_df[col] = df[col].apply(lambda x: str(int(x)) if isinstance(x, float) and x.is_integer() else (str(x)).strip() if pd.notnull(x) else x)

    return cleaned_df
        