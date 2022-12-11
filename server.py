import time
import os
import flask

from flask import g
from chat2gpt import chat_with_GPT

APP = flask.Flask(__name__)

tool = chat_with_GPT()

@APP.route("/chat", methods=["GET"])
def chat():
    message = flask.request.args.get("q")
    print("Sending message: ", message)
    global tool
    try:
        response = tool.chat2GPT(message)
    except Exception as e:
        print('error:', e)
        print('reset context')
        tool = chat_with_GPT()
        response = tool.chat2GPT(message)
    # response = tool.chat2GPT(message)
    print("Response: ", response)
    return response

def start_browser():
    APP.run(host = '0.0.0.0', port=5001, threaded=False)

if __name__ == "__main__":
    start_browser()
