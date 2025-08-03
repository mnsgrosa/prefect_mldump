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
    caller = ApiCaller(data = data)
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
    sumarization = summarize(**data)
    return sumarization

@task
def items_to_post(sumarization):
    stored = httpx.get('http://localhost:8000/get').json()
    to_post = []

    for key in sumarization.keys():
        if key not in stored.title:
            to_post.append(sumarization[key])

    return to_post

@task
def post_items(items_to_post):
    try:
        httpx.post('http://localhost:8000/post', json = {'items': items_to_post})
        return Completed(message = 'New posts added')
    except execpt as e:
        return Failed(message = f'No new post was added due to: {e}')

@flow(log_prints = True)
def post_flow(summarization):
    items_to_post = items_to_post(sumarization)
    post_items(items_to_post)

@task
def save_csv(sumarization):
    sumarization_temp = {'title': [], 'url': [], 'author': [], 'upvotes': [], 'downvotes': []}
    for key in sumarization.keys():
        sumarization_temp['title'].append(key)
        sumarization_temp['url'].append(sumarization[key]['url'])
        sumarization_temp['author'].append(sumarization[key]['author'])
        sumarization_temp['upvotes'].append(sumarization[key]['votes']['upvotes'])
        sumarization_temp['downvotes'].append(sumarization[key]['votes']['downvotes'])

    df = pd.DataFrame(sumarization_temp)
    df.to_csv('./sumarization.csv')