
from chatterbot.trainers import ListTrainer

def trainClassroom( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'dvorana 9',
		'Dvorana 9 nalazi se ...'
	])

	chatbot.train([
		'b9',
		'Dvorana 9 nalazi se ...'
	])

	chatbot.train([
		'9',
		'Dvorana 9 nalazi se ...'
	])
