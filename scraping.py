from random import sample

from pyfinviz.news import News


N_HEADLINES = 25


def get_headlines(n=N_HEADLINES) -> list:
    headlines = list(News().news_df["Headline"])
    n_headlines = sample(headlines, n) if len(headlines) > n else headlines
    return n_headlines
