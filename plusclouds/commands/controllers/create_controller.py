from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway


class CreateController(AbstractController):
	parameter_types = [ParameterType.plusclouds_api_path]

	def execute_command(self, *args, **kwargs):
		path = self.get_parameter_values(**kwargs)[0]

		http_gateway = HttpGateway()

		#
		#
		#

		resp = http_gateway.post(path).json()

		print(resp)
