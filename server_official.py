import time
import os
import flask

from flask import g
from chat2gpt import chat_with_GPT
import requests
import pandas as pd
import time
import os

APP = flask.Flask(__name__)

tool = chat_with_GPT()
user_info = {}

 # 存档每次调用，若第一次调用，创建表头
# 创建表头
if not os.path.exists('all_request.csv'):
    answerData_init = pd.DataFrame(
    columns=(
        'time', 'user', 'question', 'answer'))
    answerData_init.to_csv(f'all_request.csv', mode='a', encoding='utf-8', index=False, header = True)

@APP.route("/chat_post", methods=["POST"])
def chat_post():
    if flask.request.method == 'POST':

        ## 获取请求体信息
        message = flask.request.json.get('message')
        message.lstrip('@ChatGPT_PRO ')
        if message == 'enter_chat':
            return ''

        
        # 用户id
        user = flask.request.json.get('user')

        if message == '#new' and user in user_info:
            del user_info[user]
        assert message # 信息一定存在

        # 默认使用我自己的API KEY
        YOUR_API_KEY = flask.request.json.get('YOUR_API_KEY', 'sk-OSyJfpbIkUGzmI7T3BlbkFJolE4eWg268YvtD9DZmuJ')
        # 默认使用 gpt-3.5-turbo 模型
        model = flask.request.json.get('model', 'gpt-3.5-turbo')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + YOUR_API_KEY,
        }

        # 如果是新用户 初始化背景
        if user not in user_info:
            user_info[user + '_system'] = [{"role": "system", "content": "You are a helpful assistant."},]
            user_info[user] = []

        # 累加历史消息, 保留系统背景和最近7条，加上新问题共8条上下文
        all_message = user_info[user + "_system"] + user_info[user][-7:] + [{"role": "user", "content": message},]
        print('--'*20)
        print('user:', user)
        print('all_message before sent:', all_message)


        # 具体的对话内容
        json_data = {
            'model': model,
            'messages': all_message
        }
        ## 示例，system代表背景
        # [
        # {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Who won the world series in 2020?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
        # ]

        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
        print('response:', response.json())
        answer = response.json()['choices'][0]['message']['content']
        all_message = all_message + [{"role": "assistant", "content": answer},]
        ## 更新该用户的上下文环境
        user_info[user] = all_message[1:]
        print('all_message after sent:', all_message)

        # 将数据归档 'time', 'user', 'question', 'answer'
        row = {'time': [str(time.time())],
               'user': [user],
               'question': [message],
               'answer': [answer],
               }
        answerData = pd.DataFrame(
        columns=(
            'time', 'user', 'question', 'answer'))
        answerData = answerData.append(pd.DataFrame(row), ignore_index=True)
        answerData.to_csv(f'all_request.csv', mode='a', encoding='utf-8', index=False, header = False)
        
        return answer


def start_browser():
    APP.run(host = '0.0.0.0', port=5001, threaded=False)

if __name__ == "__main__":
    start_browser()
