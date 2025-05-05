from sklearn.linear_model import LinearRegression

def train_model(X, y):
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_next_month(model, X):
    # Predict the next month's rent
    # Assuming the latest month and year data is available
    last_month = X.iloc[-1]
    next_month_features = [[last_month['Year'], last_month['MonthNumber'] + 1]]
    
    return model.predict(next_month_features)[0]
