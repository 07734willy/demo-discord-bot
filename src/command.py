from game import create_game, guess_number, show_help
from traceback import format_exc

"""
/newgame
/guess number
/help
"""

COMMAND_PREFIX = "/"


def parse_command(msg):
	text = msg.content

	if not text.startswith(COMMAND_PREFIX):
		return

	command_text = text[len(COMMAND_PREFIX):]
	cmd, *args = command_text.split(" ")

	return cmd, args

async def dispatch_command(client, msg, cmd, args):
	command_table = {
		"newgame": create_game,
		"guess": guess_number,
		"help": show_help,
	}

	try:
		handler = command_table[cmd]
		await handler(client, msg, *args)
	except Exception as e:
		await msg.channel.send(format_exc())

async def run_command(client, msg):
	try:
		cmd, args = parse_command(msg)
	except TypeError:
		return

	await dispatch_command(client, msg, cmd, args)
	
