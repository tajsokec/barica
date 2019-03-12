
from chatterbot.trainers import ListTrainer

def trainSchedule( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'informacijski i poslovni sustavi 11 preddiplomski',
		'Za koju godinu studija trebaš raspored?'
	])

	chatbot.train([
		'informacijski poslovni su ustali 11 preddiplomski',
		'Za koju godinu studija trebaš raspored?'
	])

	chatbot.train([
		'informacijski poslovni sustav i ja točka 1 preddiplomski',
		'Za koju godinu studija trebaš raspored?'
	])

	chatbot.train([
		'informacijski poslovni sustav i 11 preddiplomski',
		'Za koju godinu studija trebaš raspored?'
	])

	chatbot.train([
		'informacijski poslovni sustav i 113 francuski',
		'Za koju godinu studija trebaš raspored?'
	])

	chatbot.train([
		'Prva',
		'Za koji grupu trebaš raspored?'
	])

	chatbot.train([
		'prvu',
		'Za koji grupu trebaš raspored?'
	])

	chatbot.train([
		'g11',
		'Izvoli raspored..'
	])

	chatbot.train([
		'g 1.1',
		'Izvoli raspored..'
	])

	
