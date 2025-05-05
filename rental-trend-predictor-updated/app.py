import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model import preprocess, model
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Rental Trend Predictor", layout="wide")

# Navigation - basic tabs
tab1, tab2, tab3 = st.tabs(["📊 Prediction", "📈 Visualization", "📋 Evaluation"])

# Load built-in dataset
df = pd.read_csv("data/rent_prices.csv")
processed_df, X, y = preprocess.prepare_data(df)
reg_model = model.train_model(X, y)
next_month = model.predict_next_month(reg_model, X)
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
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=processed_df, x="MonthNumber", y="AvgRent", hue="City", marker="o", ax=ax)
    ax.set_title("Average Rent Over Time by City")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Average Rent ($)")
    st.pyplot(fig)

# Tab 3: Model Evaluation
with tab3:
    st.title("📋 Model Evaluation Metrics")
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    st.write(f"🔹 **Mean Squared Error (MSE):** {mse:.2f}")
    st.write(f"🔹 **R² Score:** {r2:.4f}")
    st.line_chart({"Actual": y, "Predicted": y_pred})