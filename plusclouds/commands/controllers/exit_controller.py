import sys

from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.util.token_util import set_token


class ExitController(AbstractController):
	parameter_types = []

	def execute_command(self, *args, **kwargs):
		sys.exit(0)
