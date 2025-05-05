# 🏡 Rental Trend Predictor

**Predict future rental trends across cities using Linear Regression, built with Streamlit.**  
This app analyzes historical rent data and predicts the next month's average rent while showing performance metrics and visualizing trends beautifully.

> ✅ Fully automatic — no need to upload data  
> ✅ Built-in CSV dataset  
> ✅ Linear regression with evaluation  
> ✅ Deployed on Streamlit Cloud  

🚀 **Live App:** [https://your-username-rental-trend-predictor.streamlit.app](https://your-username-rental-trend-predictor.streamlit.app)

---

## ✨ Features

- 📁 **Built-in dataset** for 5 cities (no file upload required)
- 🧹 Clean preprocessing (month conversion, encoding)
- 🤖 Linear regression for predicting future rent
- 📈 Interactive trend visualization (Seaborn & Matplotlib)
- 📊 Evaluation metrics: **MSE**, **R² Score**
- 🧭 Simple tabbed navigation UI using Streamlit

---

## 🧠 How It Works

1. Reads monthly rent CSV file from internal storage
2. Preprocesses months and city labels into numerical form
3. Trains a **Linear Regression** model on the data
4. Predicts next month’s average rent per city
5. Evaluates model accuracy using:
   - **Mean Squared Error (MSE)**
   - **R² Score**
6. Visualizes rental trends over time using **Seaborn**

---

## 📁 Project Structure

```
rental-trend-predictor/
├── app.py
├── requirements.txt
├── rent_prices.csv
├── README.md
└── model/
    ├── preprocess.py
    └── model.py
```

---

## 🚀 Deployment on Streamlit Cloud

1. Upload this project to your GitHub repo
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your GitHub and choose:
   - Repository: `your-repo-name`
   - Branch: `main`
   - File: `app.py`
4. Click **Deploy**

---

## 🙋‍♂️ Author

Made with 💡 and ☕ by [Your Name](https://github.com/yourusername)