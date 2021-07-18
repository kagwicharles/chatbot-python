from flask import Flask, json, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

chatbot = ChatBot('Ron')
conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"I'm doing great.",
"That is good to hear",
"Thank you.",
"You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

api = Flask(__name__)

@api.route('/chatbot', methods=['POST'])
def get_companies():
	message = request.form.get('message')
	bot_input = chatbot.get_response(message)
	companies = {"message": str(bot_input)}
	return json.dumps(companies)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000)
