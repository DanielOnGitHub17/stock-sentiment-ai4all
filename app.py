import math

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from scraping import get_headlines
from prediction import predict

N_HEADLINES = 25
LINE_BREAK_COUNT = 3

def display_heading():
    st.title("Today's Market Prediction")
    st.markdown("""
Model that can provide stock market overview based on top news headlines
""")

    st.header("News Headlines for today")


def display_headlines():
    count = 0
    headlines = get_headlines(N_HEADLINES)
    columns = st.columns(N_HEADLINES)
    headlines_display = headlines.copy()
    while headlines_display:
        columns = st.columns(2)
        for col in columns:
            with col:
                st.text(headlines.pop())
            if not headlines_display:
                return headlines
    return headlines

display_prediction_button(headlines):
    if st.button("Generate stock overview"):
        # Go to finviz, scrape for input. Feed to model return answer as binary type.
        result = predict(
            np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
        st.text(result[0])

        # Display the image/icon corresponding to the predicted class
        image_path = class_to_image(result[0].split("-")[1])
        st.image(image_path, use_column_width=True)


display_heading()
st.text("")
headlines = display_headlines()
st.text("")
display_prediction_button(headlines)
st.text("")