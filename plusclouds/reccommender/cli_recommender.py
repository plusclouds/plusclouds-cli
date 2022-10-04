from plusclouds.options.options_parser import OptionsParser
import readline
from plusclouds.commands.command_binder import available_commands

readline.parse_and_bind("tab: complete")


class CLIRecommender:
	def __init__(self):
		self.option_parser = OptionsParser.get_instance()

	def complete(self, text, state):
		line = readline.get_line_buffer()

		if line == "" or (len(line.strip().split(" ")) == 1 and line[-1] != " ") or len(line.strip()) == 0:
			return list(available_commands.keys())[state]

		# For recommending API Path parameters
		try:
			if len(line) > 0:
				tokens = line.split(" ")
				tokens.pop(0)
				try:
					if len(tokens) > 1 or (len(line.strip()) != 0 and line[-1] == " "):
						self.option_parser.alter_directory(tokens)
				except Exception as e:
					pass

			try:
				if len(line.strip()) == 0 or line[-1] == " ":
					return self.option_parser.recommend("")[state]
			except Exception as e:
				pass

			return self.option_parser.recommend(text.strip())[state]
		except Exception as e:
			pass
