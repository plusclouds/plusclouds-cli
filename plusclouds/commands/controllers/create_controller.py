from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway
from plusclouds.options.options_parser import OptionsParser
from tests.command_tests.option_test import option_data


class CreateController(AbstractController):
	parameter_types = [ParameterType.plusclouds_api_path]

	def execute_command(self, *args, **kwargs):
		path = self.get_parameter_values(**kwargs)[0]

		http_gateway = HttpGateway()

		#options_parser = OptionsParser.get_instance()

		resp = option_data  # Start here

		results = {}


		for key, value in resp["methods"]["POST"]["fields"][0].items():

			if value.startswith("required"):
				while True:
					try:
						results[key] = input(key.capitalize() + " : ")
						if results[key] != "":
							break;
						else:
							print(key + " is required! Please enter a valid " + key + ".")
					except ValueError:
						print("Invalid")
						continue
			else:
				results[key] = input(key.capitalize() + " : ")
				results[key] = results[key] if results[key] != "" else None

		print(results)
		resp = http_gateway.post(path, body=results).json()

		print(resp)
