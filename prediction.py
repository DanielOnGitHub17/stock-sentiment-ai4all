"""Module to predict stock from data"""

def predict(data):
    clf = joblib.load("stock-sentiment-predict.pkl")
    return clf.predict(data)

def array_to_input(array):
    pass