from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


def trainBot(chatbot):
    conversation = [
        "Watu wa stima",
        "Wacha mambo ya stima wewe?",
        "Mambo ya stima achia watu wa stima",
        "Nitakufinya",
        "Finya",
        "Nitakufinya",
        "Finya",
        "Nitakufinya."
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    return chatbot
