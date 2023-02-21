from revChatGPT.V1 import Chatbot
import json

# Get your config in JSON
class chat_with_GPT():
    def __init__(self, config = 'config.json'):
        with open(config, 'r') as fr:
            self.config = json.load(fr)

        self.chatbot = Chatbot(self.config, conversation_id=None)
        self.chatbot.reset_chat() # Forgets conversation
        # self.chatbot.refresh_session() # Uses the session_token to get a new bearer token

    def chat2GPT(self, message):
        # resp = self.chatbot.get_chat_response(message, output="text")
        for data in self.chatbot.ask(
        message
        ):
            response = data["message"]
        return response

if __name__ == '__main__':
    tool = chat_with_GPT()
    print(tool.chat2GPT('hello'))
