import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model import preprocess, model
from sklearn.metrics import mean_squared_error, r2_score

# Set page configuration
st.set_page_config(page_title="Rental Trend Predictor", layout="wide")

# Navigation - basic tabs
tab1, tab2, tab3 = st.tabs(["📊 Prediction", "📈 Visualization", "📋 Evaluation"])

# Load built-in dataset from root
df = pd.read_csv("rent_prices.csv")

# Data Preprocessing
processed_df, X, y = preprocess.prepare_data(df)

# Train the Model
reg_model = model.train_model(X, y)

# Predict next month's rent
next_month = model.predict_next_month(reg_model, X)

# Predictions for model evaluation
y_pred = reg_model.predict(X)

# Tab 1: Prediction Output
with tab1:
    st.title("🏠 Rental Trend Predictor")
    st.write("Using historical rent data to predict next month's average rent.")
    st.dataframe(df.head(10))
    st.success(f"📌 Predicted Next Month's Average Rent: **${next_month:.2f}**")

# Tab 2: Visualization
with tab2:
    st.title("📈 Rent Trends Visualization")
    
    # Convert 'Month' to datetime if not already done
    processed_df['Month'] = pd.to_datetime(processed_df['Month'])
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=processed_df, x="Month", y="AvgRent", hue="City", marker="o", ax=ax)
    ax.set_title("Average Rent Over Time by City")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Rent ($)")
    st.pyplot(fig)

# Tab 3: Model Evaluation
with tab3:
    st.title("📋 Model Evaluation Metrics")
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    st.write(f"🔹 **Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"🔹 **R² Score:** {r2:.4f}")
    
    # Plot Actual vs Predicted Rent values
    eval_fig, eval_ax = plt.subplots(figsize=(10, 5))
    eval_ax.plot(processed_df['Month'], y, label='Actual Rent', color='blue', marker='o')
    eval_ax.plot(processed_df['Month'], y_pred, label='Predicted Rent', color='orange', linestyle='--', marker='x')
    eval_ax.set_title("Actual vs Predicted Rent")
    eval_ax.set_xlabel("Month")
    eval_ax.set_ylabel("Average Rent ($)")
    eval_ax.legend()
    st.pyplot(eval_fig)
