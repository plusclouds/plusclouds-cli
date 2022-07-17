from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway
from plusclouds.handler.response_handler import response_handler


class ListController(AbstractController):
	parameter_types = [ParameterType.plusclouds_api_path]

	def execute_command(self, *args, **kwargs):
		path = self.get_parameter_values(**kwargs)[0]

		http_gateway = HttpGateway()

		resp = http_gateway.get(path)
		response_handler(resp=resp)

		# body = resp.json()
		#
		# if resp.status_code >= 400:
		# 	print("Couldn't List results please try another path.")
		# 	return
		#
		# for item in body["data"]:
		# 	print("\n".join("{} : {}".format(key, value) for key,value in item.items()))
		# 	print("\n")

