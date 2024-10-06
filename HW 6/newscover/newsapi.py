import requests

API_KEY='30ed1d954acc4412a82367f83be125d7'

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    url = f"https://newsapi.org/v2/everything?q={news_keywords}&from={lookback_days}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

