from random import sample

import requests as req
from bs4 import BeautifulSoup


N_HEADLINES = 25
FINVIZ_STOCK_URL = "https://finviz.com/news.ashx?v=3"


def get_finviz_page() -> str:
    with req.get(FINVIZ_STOCK_URL) as response:
        return response.text
    return "404"


def extract_headlines(page_text) -> list:
    soup = BeautifulSoup(page_text, 'html.parser')
    headline_elements = soup.select('.nn-tab-link')
    headlines = [headline_element.text for headline_element in headline_elements]
    return headlines


def get_headlines(n=N_HEADLINES) -> list:
    page_text = get_finviz_page()
    headlines = extract_headlines(page_text)
    n_headlines = sample(headlines, n) if len(headlines) > n else headlines
    return n_headlines
