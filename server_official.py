import time
import os
import flask

from flask import g
from chat2gpt import chat_with_GPT
import requests

APP = flask.Flask(__name__)

tool = chat_with_GPT()

@APP.route("/chat_post", methods=["POST"])
def chat_post():
    if flask.request.method == 'POST':
        # data = flask.request.get_json()
        # print('Data Received: "{data}"'.format(data=data))
        # return "Request Processed.\n"

        # curl https://api.openai.com/v1/chat/completions \
        #     -H 'Content-Type: application/json' \
        #     -H 'Authorization: Bearer YOUR_API_KEY' \
        #     -d '{
        #     "model": "gpt-3.5-turbo",
        #     "messages": [{"role": "user", "content": "Hello!"}]
        #     }'

        ## 获取请求体信息
        message = flask.request.json.get('message')
        assert message # 信息一定存在
        # 默认使用我自己的API KEY
        YOUR_API_KEY = flask.request.json.get('YOUR_API_KEY', '')
        # 默认使用 gpt-3.5-turbo 模型
        model = flask.request.json.get('model', 'gpt-3.5-turbo') 

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + YOUR_API_KEY,
        }
        
        # 具体的对话内容
        json_data = {
            'model': model,
            'messages': message
        }
        ## 示例，system代表背景
        # [
        # {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
        # ]



        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)        
        return response
    

def start_browser():
    APP.run(host = '0.0.0.0', port=5001, threaded=False)

if __name__ == "__main__":
    start_browser()
