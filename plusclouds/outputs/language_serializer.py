import json


def get_message(name, language: str = "en", default_message: str = ""):
	if language != "en" and language != "":
		print("Unsupported language")

	if type(name) == str:
		name = [name]

	file_path = "./english_outputs.json"

	file: dict = json.load(open(file_path, "r"))

	


get_message("greeting")
