import unittest
from newsapi import fetch_latest_news
import json

with open('tests_secrets.json', 'r') as file:
    secrets = json.load(file)
API_KEY = secrets['API_KEY']

class TestNewsAPI(unittest.TestCase, API_KEY):

    def test_fetch_latest_news_no_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(API_KEY, '')

    def test_fetch_latest_news_lookback_days(self):
        news = fetch_latest_news(API_KEY, 'python', lookback_days=5)
        self.assertIsNotNone(news)
        self.assertIn('articles', news)
        self.assertTrue(all(article['publishedAt'] >= '2024-08-01' for article in news['articles']))

    def test_fetch_latest_news_invalid_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(API_KEY, 'python!')

if __name__ == '__main__':
    unittest.main()
