import streamlit as st
import pandas as pd
import numpy as np
import joblib

from scraping import get_headlines
from prediction import predict

N_HEADLINES = 25

st.title("Market prediction for today")
st.markdown("""
Model that can provide stock market overview based on top news headlines
""")

st.header("News Headlines for today")
headlines = get_headlines(N_HEADLINES)
columns = st.columns(N_HEADLINES)
for col, headline in zip(columns, headlines):
    with col:
        st.text(headline)

st.text('')
if st.button("Generate stock overview"):
    # Go to finviz, scrape for input. Feed to model return answer as binary type.
    result = predict(
        np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    st.text(result[0])

    # Display the image/icon corresponding to the predicted class
    image_path = class_to_image(result[0].split("-")[1])
    st.image(image_path, use_column_width=True)


st.text('')
