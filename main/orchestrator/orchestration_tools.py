from prefect import task, flow
from api_tool import ApiCaller, ResponseNavigator
from typing import Dict, List, Any
import pandas as pd

@task
def fetch_data(subreddit: str = 'redditdev'):
    caller = ApiCaller(subreddit)
    return caller.data

@task
def fetch_urls(data: Dict[str, Any]) -> List[str]:
    caller = ResponseNavigator(data = data)
    return caller.scrape_urls()

@task
def fetch_authors(data: Dict[str, Any]) -> List[str]:
    caller = ResponseNavigator(data = data)
    return caller.scrape_authors()

@task
def fetch_titles(data: Dict[str, Any]) -> List[str]:
    caller = ResponseNavigator(data = data)
    return caller.scrape_titles()

@task
def fetch_votes(data: Dict[str, Any]) -> Dict[str, Any]:
    caller = ResponseNavigator(data = data)
    return caller.scrape_votes()

@task
def summarize(data: Dict[str, Any]) -> Dict[str, Any]:
    caller = ResponseNavigator(data)
    return caller.summarize(data)

@flow(log_prints = True)
def scrape_flow():
    data = fetch_data()
    urls = fetch_urls(data)
    authors = fetch_authors(data)
    titles = fetch_titles(data)
    votes = fetch_votes(data)
    to_sumarize = {'titles':titles, 'urls': urls, 'authors': authors, 'votes': votes}
    summarization = summarize(**to_sumarize)
    return summarization

@task
def items_to_post(summarization):
    stored = httpx.get('http://localhost:9001/get').json()
    to_post = []

    for key in sumarization.keys():
        if key not in stored.title:
            to_post.append(sumarization[key])

    return to_post

@task
def post_items(items_to_post):
    try:
        httpx.post('http://localhost:9001/post', json = {'items': items_to_post})
        return Completed(message = 'New posts added')
    except Exception as e:
        return Failed(message = f'No new post was added due to: {e}')

@flow(log_prints = True)
def post_flow(summarization):
    items_to_post = items_to_post(sumarization)
    return post_items(items_to_post)

@flow(log_prints = True)
def full_flow():
    summarization = scrape_flow()
    return post_flow(summarization)