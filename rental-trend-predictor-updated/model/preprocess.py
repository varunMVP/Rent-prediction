import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data(df):
    df['Month'] = pd.to_datetime(df['Month'])
    df.sort_values(by=['City', 'Month'], inplace=True)
    df['MonthNumber'] = df['Month'].dt.month + (df['Month'].dt.year - df['Month'].dt.year.min()) * 12
    le = LabelEncoder()
    df['CityEncoded'] = le.fit_transform(df['City'])
    X = df[['MonthNumber', 'CityEncoded']]
    y = df['AvgRent']
    return df, X, y