from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.util.token_util import set_token


class SetTokenController(AbstractController):
	parameter_types = [ParameterType.token]

	def execute_command(self, *args, **kwargs):
		token = self.get_parameter_values(**kwargs)[0]
		set_token(token)
