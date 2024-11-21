from random import sample

import requests as req
from bs4 import BeautifulSoup
from pyfinviz.news import News


N_HEADLINES = 25


def get_headlines(n=N_HEADLINES) -> list:
    headlines = News().news_df["Headline"]
    n_headlines = sample(headlines, n) if len(headlines) > n else headlines
    return n_headlines
