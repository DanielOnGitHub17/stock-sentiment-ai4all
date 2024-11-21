import math

import streamlit as st
import pandas as pd
import numpy as np
import joblib

from scraping import get_headlines
from prediction import headlines_to_input, predict

N_HEADLINES = 25
LINE_BREAK_COUNT = 3
PREDICTION_TEXTS = ("The market is not doing well today", "The market is doing well today")

def display_heading():
    """Start page content"""
    st.title("Market sentiment for today")
    st.markdown("""
Model that can provide stock market sentiment based on top news headlines
""")

    st.header("News Headlines for today")


def display_headlines():
    """Display the scraped headlines"""
    count = 0
    headlines = get_headlines(N_HEADLINES)
    columns = st.columns(N_HEADLINES)
    headlines_display = headlines.copy()
    while headlines_display:
        columns = st.columns(2)
        for col in columns:
            if not headlines_display:
                return headlines
            with col:
                st.text(headlines_display.pop())
    return headlines

def display_prediction_button(headlines):
    """Event handler for prediction button"""
    if st.button("Generate stock overview"):
        # Get Vectorized input
        data = headlines_to_input(headlines)
        result = predict(data)  # 0/1
        # Display the result text
        st.text(PREDICTION_TEXTS[result])


# Set the page title
st.set_page_config(page_title="Stock market sentiment")

display_heading()
st.text("")
headlines = display_headlines()
st.text("")
display_prediction_button(headlines)
st.text("")
