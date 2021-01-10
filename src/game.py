from random import randint

CURRENT_GAME = None

class Game(object):
	def __init__(self):
		self.number = randint(1, 100)
		self.guesses_remaining = 7
		print(f"DEBUG: secret number is {self.number}")

	async def guess(self, channel, number):
		if number == self.number:
			await channel.send("you win")
			self.endgame()
		elif number < self.number:
			await channel.send("too low")
		else:
			await channel.send("too high")

		self.guesses_remaining -= 1
		if not self.guesses_remaining:
			await channel.send("You lose!")
			self.endgame()

	def endgame(self):
		global CURRENT_GAME
		CURRENT_GAME = None

async def create_game(client, msg):
	global CURRENT_GAME
	await msg.channel.send("Created game")
	CURRENT_GAME = Game()

async def guess_number(client, msg, num_str):
	if not CURRENT_GAME:
		await msg.channel.send("No current game")
		#raise Exception()
		return
	
	number = int(num_str)
	await CURRENT_GAME.guess(msg.channel, number)

async def show_help(client, msg):
	await msg.channel.send("Showing help")
