from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.util.token_util import set_token
from plusclouds.gateway.http_client import post_dict, delete_dict, get_dict, options_dict


class SetTokenController(AbstractController):
	parameter_types = [ParameterType.token]

	def execute_command(self, *args, **kwargs):
		token = self.get_parameter_values(**kwargs)[0]
		set_token(token)
		post_dict.clear()
		delete_dict.clear()
		get_dict.clear()
		options_dict.clear()
