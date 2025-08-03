import httpx
from bs4 import BeautifulSoup
from typing import Dict, Any, List

class ApiCaller:
    def __init__(self, subreddit: str = 'redditdev'):
        self.subreddit = subreddit
        self.url = f'https://www.reddit.com/r/{self.subreddit}.json'
        self.data = self.scrape_contents()

    def scrape_contents(self):
        response = httpx.get(self.url).json()
        data = response.get('data', {})
        children = data.get('children', [])
        return children

class ResponseNavigator:
    def __init__(self, data: List[Any] = None):
        self.data = data

    def get_items(self, key: str):
        if self.data is None:
            return None
        
        return [data.get('data', {}).get(key, {}) for data in self.data]

    def scrape_urls(self):
        if self.data is None:
            return None

        self.urls = self.get_items('url')
        return self.urls

    def scrape_authors(self):
        if self.data is None:
            return None

        self.authors = self.get_items('author')
        return self.authors

    def scrape_titles(self):
        if self.data is None:
            return None
        
        self.titles = self.get_items('title')
        return self.titles

    def scrape_votes(self):
        if self.data is None:
            return None
        
        self.upvotes = self.get_items('ups', {})
        self.downvotes = self.get_items('downs', {})

        self.votes = [{'upvotes': upvotes, 'downvotes': downvotes} for upvotes, downvotes in zip(self.upvotes, self.downvotes)]
        return self.votes

    def summarize(self, titles, urls, authors, votes):
        self.sumarization = {title:{'url': url, 'author': author, 'votes': vote} for title, url, author, vote in zip(titles, urls, authors, votes)}
        return self.sumarization