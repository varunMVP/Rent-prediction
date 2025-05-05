import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv("rent_prices.csv")  # Ensure CSV file is in the root directory

# Check the columns of the dataframe
st.write(f"Columns in DataFrame: {df.columns}")

# Data preprocessing and visualization
def preprocess_data(df):
    # Ensure 'Month' column is in datetime format
    df['Month'] = pd.to_datetime(df['Month'])

    # Extract the month and year as separate columns for regression
    df['Year'] = df['Month'].dt.year
    df['Month_num'] = df['Month'].dt.month

    return df

# Linear Regression Model to Predict Rent
def predict_rent(df):
    # Extract the features and target variable
    X = df[['Year', 'Month_num']]
    y = df['Average_Rent']  # Assuming 'Average_Rent' is the column with the rent prices

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next month's rent
    next_month = pd.to_datetime(df['Month'].max()) + pd.DateOffset(months=1)
    next_month_features = pd.DataFrame({
        'Year': [next_month.year],
        'Month_num': [next_month.month]
    })

    next_month_rent = model.predict(next_month_features)[0]
    return next_month_rent

# Process the data
processed_df = preprocess_data(df)

# Predict the next month's rent
predicted_rent = predict_rent(processed_df)

# Display the predicted rent for next month
st.write(f"Predicted average rent for next month: ${predicted_rent:.2f}")

# Model Evaluation
X = processed_df[['Year', 'Month_num']]
y = processed_df['Average_Rent']
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Model Evaluation Metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

st.write(f"Model Evaluation Metrics:")
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R² Score: {r2:.2f}")

# Plot the trends using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x=processed_df['Month'], y=processed_df['Average_Rent'])
plt.title("Rent Price Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Average Rent")
plt.xticks(rotation=45)
st.pyplot(plt)
