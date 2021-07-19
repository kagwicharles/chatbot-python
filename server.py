"""

This code starts the server at any of
the computer's code and port 5000

@author Charles Kagwi

"""

from flask import Flask, json, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import train

chatbot = ChatBot('Ron')

api = Flask(__name__)

train.trainBot(chatbot)


@api.route('/chatbot', methods=['POST'])
def get_companies():
    message = request.form.get('message')
    print("From sender: "+message)
    bot_input = chatbot.get_response(message)
    companies = {"message": str(bot_input)}
    return json.dumps(companies)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
