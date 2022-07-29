from plusclouds.reccommender.cli_recommender import CLIRecommender
import readline
from plusclouds.commands.command_binder import available_commands
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway

global_http_variable = HttpGateway()


def CLI() -> None:
	completer = CLIRecommender()
	readline.set_completer(completer.complete)

	try:
		line = input('PlusClouds> ')
	except KeyboardInterrupt:
		print("\nClosing PlusClouds CLI\nHave a great day!")
		exit(0)
		return
	command_paths = line.strip().split(" ")

	if line == "":
		return

	if command_paths[0] not in available_commands.keys():
		print("Invalid Command")
		return
	command = available_commands[command_paths[0]]

	command_paths.pop(0)  # pop the command to use the parameters

	parameters = command.get_parameters()

	kwargs = {"query_parameters": {}}

	# Query Parameter / Flags get from input

	for i in range(len(command_paths)):
		if len(command_paths) > 2 and command_paths[i][:2] == "--":
			if i + 1 >= len(command_paths):
				break
			if command_paths[i + 1] == "true" or command_paths[i + 1] == "false":
				kwargs["query_parameters"][command_paths[i][2:]] = bool(str.capitalize(command_paths[i + 1]))
			else:
				kwargs["query_parameters"][command_paths[i][2:]] = command_paths[i + 1]
			command_paths.pop(i)
			command_paths.pop(i)

	for i in range(len(parameters)):
		parameter_type = parameters[i]
		if parameter_type == ParameterType.plusclouds_api_path:
			kwargs[parameter_type.name] = "/".join(command_paths)
			break

		kwargs[parameter_type.name] = command_paths[i]

	command.execute_command(**kwargs)
