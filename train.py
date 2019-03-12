
from chatterbot.trainers import ListTrainer

def train( bot ):
	chatbot = ListTrainer( bot )
	
	# reove these two lines for version 1.0.0 of chatterbot
	bot.set_trainer( ListTrainer ) #1
	chatbot = bot #2

	chatbot.train([
		'Barice',
		'Izvoli?'
	])

	chatbot.train([
		'Marice',
		'Izvoli?'
	])


	chatbot.train([
		'Zorice',
		'Izvoli?'
	])


	chatbot.train([
		'Starice',
		'Izvoli?'
	])


	chatbot.train([
		'Varice',
		'Izvoli?'
	])

	chatbot.train([
		'Reci mi nešto općenito o FOI-u',
		'Fakultet organizacije i informatike....'
	])

	chatbot.train([
		'Reci mi nešto o FOI-u',
		'Fakultet organizacije i informatike....'
	])


	chatbot.train([
		'FOI',
		'Fakultet organizacije i informatike....?'
	])


	chatbot.train([
		'Trebam naći dvoranu',
		'Koja dvorana?'
	])

	chatbot.train([
		'Trebam dvoranu',
		'Koja dvorana?'
	])

	chatbot.train([
		'Gdje je dvorana',
		'Koja dvorana?'
	])

	chatbot.train([
		'Dvorana',
		'Koja dvorana?'
	])


	chatbot.train([
		'Trebam naći profesora',
		'Koji profesor?'
	])

	chatbot.train([
		'Trebam naći jednog profesora',
		'Koji profesor?'
	])

	chatbot.train([
		'Trebam profesora',
		'Koji profesor?'
	])

	chatbot.train([
		'Profesor',
		'Koji profesor?'
	])

	chatbot.train([
		'Trebam raspored',
		'Za koji vrstu studija trebaš raspored?'
	])

	chatbot.train([
		'Molim raspored',
		'Za koji vrstu studija trebaš raspored?'
	])

	chatbot.train([
		'Trebam svoj raspored',
		'Za koji vrstu studija trebaš raspored?'
	])

	chatbot.train([
		'Molim te raspored',
		'Za koji vrstu studija trebaš raspored?'
	])

	chatbot.train([
		'Raspored',
		'Za koji vrstu studija trebaš raspored?'
	])

