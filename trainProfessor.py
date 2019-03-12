
from chatterbot.trainers import ListTrainer

def trainProfessor( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'Zlatko Stapić',
		'Profesor Zlatko Stapić nalazi se ..'
	])

	chatbot.train([
		'Profesor Zlatko Stapić',
		'Profesor Zlatko Stapić nalazi se ..'
	])

	chatbot.train([
		'Zlatko Savić',
		'Profesor Zlatko Stapić nalazi se ..'
	])

	chatbot.train([
		'Stapić',
		'Profesor Zlatko Stapić nalazi se ..'
	])
