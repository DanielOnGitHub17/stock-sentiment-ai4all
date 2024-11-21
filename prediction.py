"""Module to predict stock from data"""
import re
import joblib
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


# Load the model - for Python to cache it.
STOCK_SENTIMENT_PREDICTOR = joblib.load("stock-sentiment-predict.joblib")

def predict(vectorized_headlines):
    """Function to predict using model"""
    stock_model = STOCK_SENTIMENT_PREDICTOR
    prediction = stock_model.predict(vectorized_headlines)
    return prediction

def headlines_to_input(headlines):
    # Make count vectorizer
    countvector = CountVectorizer(ngram_range=(2, 2))
    # Combine headlines, make lower case, remove anything that's not text
    headlines_combined = [re.sub(r"[^a-zA-Z]", ' ', ' '.join(headlines).lower())]
    vectorized_headlines = countvector.fit_transform(headlines_combined)
    return vectorized_headlines
