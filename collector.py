import os
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def get_ai_news():

    articles = newsapi.get_everything(
        q="Artificial Intelligence OR AI",
        language="en",
        sort_by="publishedAt",
        page_size=10,
    )

    results = []

    for article in articles["articles"]:
        results.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "published": article["publishedAt"],
            "url": article["url"]
        })

    return results