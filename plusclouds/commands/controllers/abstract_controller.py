from plusclouds.exceptions.not_implemented_exception import NotImplementedException
from plusclouds.exceptions.parameter_exception import ParameterException
from typing import List
from plusclouds.enums.parameter_types import ParameterType


class AbstractController:
	parameter_types: List[ParameterType] = []

	def get_parameters(self) -> List[ParameterType]:
		return self.parameter_types

	def get_parameter_values(self, **kwargs):
		params = self.get_parameters()

		parameter_value = []
		for param_type in params:
			try:
				current_param = kwargs[param_type.name]
			except KeyError as e:
			#	print("{} Parameter doesn't exist on the command.".format(e.__str__()))
				parameter_value.append("")

				continue

			parameter_value.append(current_param)

		return parameter_value

	def execute_command(self, *args, **kwargs):
		raise NotImplementedException("Command is Not Implemented")
