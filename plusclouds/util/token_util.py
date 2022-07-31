import os.path

token_id = 1


def set_token(token: str):
	file_object = open('authorized_token', 'w')
	file_object.write(token)
	file_object.close()

	global token_id
	token_id += 1


def get_token() -> (str, bool):
	token = ""
	if os.path.exists('authorized_token'):
		file_object = open('authorized_token', 'r')
		token = file_object.readlines()[0]
		file_object.close()

	return token, (token != "")
