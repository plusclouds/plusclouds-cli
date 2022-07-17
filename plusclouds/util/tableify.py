def get_data_row(key, data):
	return "| " + str(key) + " : " + str(data) + " |"


def max_line_length_calc(key, data):
	return len(get_data_row(key, data))


def draw_line(len):
	line = ""
	for i in range(len):
		line += "-"
	return line


def tableify(data: dict):
	max_line_len = 0
	obj = {}
	for key, data in data.items():
		obj[key] = data
		current_len = max_line_length_calc(key, data)
		if max_line_len < current_len:
			max_line_len = current_len
	print(draw_line(max_line_len))
	for key, data in obj.items():
		print(get_data_row(key,data))
		print(draw_line(max_line_len))

