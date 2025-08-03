from fastapi import FastAPI
from typing import Dict, Any
import uvicorn
import os
import pandas as pd

app = FastAPI()

if os.path.exists('./sumarization.csv'):
    df = pd.read_csv('./sumarization.csv')
else:
    df = pd.DataFrame()

@app.get('/get')
def get_data():
    return {'df': df}

@app.post('/post')
def post_data(data: Dict[str, Any]):
    try:
        transformed_data = {'title': [], 'url': [], 'author': [], 'upvotes': [], 'downvotes': []}
        for item in data.keys():

            transformed_data['title'].append(item)
            transformed_data['url'].append(data[item]['url'])
            transformed_data['author'].append(data[item]['author'])
            transformed_data['upvotes'].append(data[item]['votes']['upvotes'])
            transformed_data['downvotes'].append(data[item]['votes']['downvotes'])

        df_temp = pd.DataFrame(transformed_data)
        df.append(df_temp)
        df.to_csv('./sumarization.csv', indxe = False)

        return {'status':'success'}
    except Exception as e:
        return {'status':'error {e}'}

if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 9001)