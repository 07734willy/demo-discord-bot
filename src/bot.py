from discord import Client, Intents

from traceback import format_exc
import os
import asyncio

from command import run_command

TOKEN = os.getenv('DEMO_BOT_TOKEN')

class CustomClient(Client):
	
	async def on_ready(self):
		print("Bot has connected")

	async def on_message(self, message):
		print("Bot has noticed a message")

		await run_command(self, message)
		

def main():
	intents = Intents.default()
	intents.members = True

	client = CustomClient(intents=intents)
	client.run(TOKEN)

if __name__ == "__main__":
	main()
