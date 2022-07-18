from plusclouds.handler.status_code_handler import status_code_handler
from plusclouds.util.tableify import tableify
from tabulate import tabulate


@status_code_handler
def response_handler(resp):
	body = resp.json()

	if "data" not in body.keys():
		print("Data does not exists within response.")
		return

	if type(body["data"]) == dict:
		item_response_handler(body["data"])

	if type(body["data"]) == list:
		list_response_handler(body["data"])


def item_response_handler(data):
	if type(data) != dict:
		print("Serialization error, please try again.")
		return
	tableify(data)


def list_response_handler(data_list):
	if len(data_list) == 0:
		print("-----------List Empty------------")
		return

	if len(data_list) > 6:
		for data in data_list:
			item_response_handler(data)
		return

	final_data = []
	for i in range(len(data_list)):
		current_data = []

		for key, data in data_list[i].items():
			current_data.append(data)
			if data is None:
				continue
		final_data.append(current_data)

	col_names = data_list[0].keys()

	print(tabulate(final_data, headers=col_names, tablefmt="plain"))
