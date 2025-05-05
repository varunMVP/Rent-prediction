# 🏠 Rental Trend Predictor

The **Rental Trend Predictor** is a smart web application that predicts the **average rent for the upcoming month** based on historical rental data. It uses machine learning techniques to learn from past trends and gives insights into city-wise rental behavior over time.

> 🚀 Built with **Python, Streamlit, Pandas, Scikit-learn, Seaborn, and Matplotlib**.

---

## 💡 What It Does

- 📊 **Predicts next month's average rent** using Linear Regression.
- 📈 **Visualizes rent trends over time**, city-wise.
- 📋 **Evaluates prediction performance** using MSE and R² metrics.
- 🖼️ **Interactive UI** with tab-based navigation for prediction, visualization, and evaluation.

---

## 🌐 How It Works

### 1. **Data Processing**
- The app starts by loading rental data from a CSV file (`rent_prices.csv`) containing:
Month,City,AvgRent
2023-01,CityA,1200
2023-01,CityB,1300
...
- Dates are parsed and split into **year and month numbers** to help the model understand time-series behavior.

---

### 2. **Machine Learning Model**
- A **Linear Regression model** is trained on historical rent data.
- The model learns the pattern of rent changes over months and years.
- It **predicts the rent for the next month**, using the most recent date as the reference.

---

### 3. **Streamlit App UI**
The app is structured with three interactive tabs:

#### 📊 Prediction
- Displays the dataset and the **predicted rent for next month**.
- Offers a clear view of how past data drives future predictions.

#### 📈 Visualization
- Graphs rent changes over time, **differentiated by cities**.
- Uses **Seaborn line plots** to highlight month-on-month variation.

#### 📋 Evaluation
- Shows **Mean Squared Error (MSE)** and **R² Score**.
- Compares **actual vs predicted rent** using graphs.
- Helps understand how accurate the model is.

---

## 🔍 Sample Output Screenshots

> You can upload screenshots in your repository and embed them like this:

### 🖼️ Prediction Tab
![Image](https://github.com/user-attachments/assets/fb4853c4-1a12-48f6-b25c-62bb4cb48b1f)

### 📈 Visualization Tab
![Image](https://github.com/user-attachments/assets/dea1f742-02ab-42a5-acf8-5e95c48cff76)

### 📋 Evaluation Tab
![Image](https://github.com/user-attachments/assets/80f23f91-1c3b-4fe5-a27e-367afbc4b17f)



## 🎯 Why It Matters

Rent prediction helps:
- Tenants plan budgets with foresight.
- Landlords adjust pricing smartly.
- Analysts observe city-wise housing market trends.

This project demonstrates how **data-driven insights** can be transformed into an **interactive predictive tool** for real-world decision-making.

---

## 🤖 Tech Stack

| Technology       | Role                                |
|------------------|-------------------------------------|
| **Python**       | Backend logic, data processing      |
| **Pandas**       | DataFrame manipulation              |
| **Scikit-learn** | Machine learning model              |
| **Streamlit**    | Web interface                       |
| **Matplotlib & Seaborn** | Data visualization          |

---

## 📦 Project Structure

├── app.py # Main Streamlit app
├── rent_prices.csv # Rental dataset
├── model/
│ ├── model.py # ML model logic
│ └── preprocess.py # Data preprocessing
├── screenshots/ # UI screenshots (add here)
└── README.md # You are here!

---

## 🙌 Credits

This project was developed as part of a real-world application to demonstrate **predictive analytics in rental housing markets** using accessible technologies.

Feel free to fork, extend, or contribute!
