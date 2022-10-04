import random

from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.enums.parameter_types import ParameterType
from plusclouds.gateway.http_client import HttpGateway
from plusclouds.handler.response_handler import response_handler

class UploadTokenController(AbstractController):
	parameter_types = [ParameterType.email, ParameterType.folder_path]

	def execute_command(self, *args, **kwargs):
		email = self.get_parameter_values(**kwargs)[0]
		token_path = self.get_parameter_values(**kwargs)[1]

		http_gateway = HttpGateway()

		if (token_path == ""):
			token_path = "~/.ssh/id_rsa.pub"

		try:
			token = open(token_path, "r").read()
		except FileNotFoundError as e:
			print("File not found. Please provide a valid path.")
			return

		results = {
			"name"               : "cli_ssh_key_{}".format(random.randrange(1000, 9999)),
			"public_key"         : token,
			"ssh_encryption_type": "ssh-rsa",
			"email"              : email
		}

		resp = http_gateway.post("iaas/ssh-keys", body=results)

		response_handler(resp=resp)

