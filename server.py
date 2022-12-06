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
    response = tool.chat2GPT(message)
    print("Response: ", response)
    return response

def start_browser():
    APP.run(host = '0.0.0.0', port=5001, threaded=False)

if __name__ == "__main__":
    start_browser()
