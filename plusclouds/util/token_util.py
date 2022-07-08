import os.path


def set_token(token: str):
	file_object = open('authorized_token', 'w')
	file_object.write(token)
	file_object.close()


def get_token() -> (str, bool):
	token = ""
	if os.path.exists('authorized_token'):
		file_object = open('authorized_token', 'r')
		token = file_object.readlines()[0]
		file_object.close()

	return token, (token != "")
