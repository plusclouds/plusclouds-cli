import json


def get_data_row(key, data):
	return "| {: <45} : {: <45} |".format(str(key), str(data))


def max_line_length_calc(key, data):
	return 100


def draw_line(len):
	line = ""
	for i in range(len):
		line += "="
	return line


def tableify(data, tabs: str = ""):
	if type(data) is not dict:
		if type(data) is list:
			for list_item in data:
				tableify(list_item, tabs + "\t")

		if type(data) is str or type(data) is int or type(data) is float:
			print(tabs + str(data))

		return

	for key, item in data.items():
		if type(item) is list or type(item) is dict:
			print(tabs + draw_line(97))
			print(tabs + key + ":")
			tableify(item, tabs + "\t")
			return

		print(tabs + draw_line(97))
		print(tabs + get_data_row(key, item))
	print(tabs + draw_line(97))
