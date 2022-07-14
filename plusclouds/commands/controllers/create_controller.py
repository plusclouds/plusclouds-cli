from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway
from plusclouds.options.options_parser import OptionsParser


class CreateController(AbstractController):
	parameter_types = [ParameterType.plusclouds_api_path]

	def execute_command(self, *args, **kwargs):
		path = self.get_parameter_values(**kwargs)[0]

		http_gateway = HttpGateway()

		options_parser = OptionsParser.get_instance()

		resp = options_parser.latest_response  # Start here

		results = {}

		for key, value in resp["methods"]["POST"][0].items():
			print(key + " : ")
			results[key] = input()

		resp = http_gateway.post(path, body=results).json()

	#	print(resp)
