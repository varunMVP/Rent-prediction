from sklearn.linear_model import LinearRegression

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_next_month(model, X):
    last = X.iloc[-1]
    next_month = [last['MonthNumber'] + 1, last['CityEncoded']]
    return model.predict([next_month])[0]