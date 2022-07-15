from plusclouds.reccommender.cli_recommender import CLIRecommender
import readline
from plusclouds.commands.command_binder import available_commands
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway

global_http_variable = HttpGateway()


def CLI() -> None:
	completer = CLIRecommender()
	readline.set_completer(completer.complete)

	line = input('PlusClouds> ')

	command_paths = line.strip().split(" ")

	if line == "":
		return

	if command_paths[0] not in available_commands.keys():
		print("Invalid Command")
		return
	command = available_commands[command_paths[0]]

	command_paths.pop(0)  # pop the command to use the parameters

	parameters = command.get_parameters()

	kwargs = {}

	for i in range(len(parameters)):
		parameter_type = parameters[i]
		if parameter_type == ParameterType.plusclouds_api_path:
			kwargs[parameter_type.name] = "/".join(command_paths)
			break

		kwargs[parameter_type.name] = command_paths[i]

	command.execute_command(**kwargs)
