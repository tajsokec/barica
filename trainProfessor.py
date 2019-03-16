
from chatterbot.trainers import ListTrainer

from ScrapProfesssors import *
professors = scrapProfessors()

def trainProfessor( bot ):
        chatbot = ListTrainer( bot )

        # reove these two lines for version 1.0.0 of chatterbot
        bot.set_trainer( ListTrainer ) #1
        chatbot = bot #2

        for name, user_name in professors.items():
                chatbot.train([
                name,
                user_name
                ])
                word_list = name.split()
                chatbot.train([
                word_list[-1],
                user_name
                ])                
                if 'nastavnici' or 'sluzbe' in user_name:
                        if name.split(' ', 1)[0].endswith('a'):
                                chatbot.train([
                                'profesorica ' + name,
                                user_name
                                ])
                        else:
                                chatbot.train([
                                'profesor ' + name,
                                user_name
                                ])
