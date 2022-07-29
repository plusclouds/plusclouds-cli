from typing import Dict

from plusclouds.commands.controllers.token_controller import SetTokenController
from plusclouds.commands.controllers.list_controller import ListController
from plusclouds.commands.controllers.create_controller import CreateController
from plusclouds.commands.controllers.exit_controller import ExitController
from plusclouds.commands.controllers.ssh_controller import SSHController
from plusclouds.commands.controllers.abstract_controller import AbstractController

available_commands: Dict[str, AbstractController] = {
	"set-token": SetTokenController(),
	"list"     : ListController(),
	"create"   : CreateController(),
	"exit"     : ExitController(),
	"ssh"      : SSHController()
}
