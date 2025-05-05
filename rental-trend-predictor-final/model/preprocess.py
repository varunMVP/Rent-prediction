import pandas as pd

def prepare_data(df):
    # Convert 'Month' to datetime if not already done
    df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')

    # Extract year and month number for prediction
    df['Year'] = df['Month'].dt.year
    df['MonthNumber'] = df['Month'].dt.month
    
    X = df[['Year', 'MonthNumber']]
    y = df['AvgRent']  # 'AvgRent' as per the CSV column name

    return df, X, y
