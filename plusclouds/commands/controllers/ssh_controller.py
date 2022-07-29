import paramiko

from plusclouds.commands.controllers.abstract_controller import AbstractController
from plusclouds.gateway.http_client import HttpGateway
from simple_term_menu import TerminalMenu

from paramiko import SSHClient, AutoAddPolicy


class SSHController(AbstractController):
	parameter_types = []

	def execute_command(self, *args, **kwargs):
		base_url = "iaas/virtual-machines?page=7&status=running"
		http_gateway = HttpGateway()

		selected = "none"
		pagination_keys = ["none"]
		page_query = ""

		while selected in pagination_keys:
			url = base_url + "&" + page_query
			pagination_keys = []

			resp = http_gateway.get(url)
			status_code = resp.status_code
			resp = resp.json()
			names = []

			if str(status_code)[0] != "2" or len(resp["data"]) == 0:
				print(resp)
				print("No Virtual Machine Available")
				return

			for vm in resp["data"]:
				names.append(vm["name"])

			if "meta" in resp.keys() and "pagination" in resp["meta"].keys() and "links" in resp["meta"][
				"pagination"].keys():
				for key in resp["meta"]["pagination"]["links"].keys():
					names.append(key)
					pagination_keys.append(key)

			terminal_menu = TerminalMenu(names)
			menu_entry_index = terminal_menu.show()
			selected = names[menu_entry_index]

			if selected in pagination_keys:
				page_query = resp["meta"]["pagination"]["links"][selected].split("&")[1]
			else:
				selected = resp["data"][menu_entry_index]

		if type(selected) != dict and "ip_addr" not in selected.keys() and "username" not in selected.keys() and "password" not in selected.keys():
			print("An error occured with the selected VM object results")
			return

		selected: dict

		username = selected["username"]
		if "USERNAME NOT ENTERED" in username:
			username = "root"
		password = selected["password"]
		if "PASSWORD NOT ENTERED" in password:
			password = "template1"

		ip_addr = selected["virtualNetworkCards"]["data"][0]["ipList"]["data"][0]["ip_addr"]

		client = SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(AutoAddPolicy())
		print("Trying to Connect to Client. {} {} {}".format(username, ip_addr, password))
		client.connect(ip_addr, username=username, password=password)
		print("Connected to {}@{}", username, ip_addr)
		user_input = ""
		conn = client.invoke_shell()
		while user_input != "exit":
			print(conn.recv(5000).decode())
			user_input = input("<<PlusClouds>> $")
			conn.send((user_input + "\n").encode())
