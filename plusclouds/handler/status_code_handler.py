def status_code_handler(func):
	def check_status_code(*args, **kwargs):
		resp = kwargs["resp"]
		body = resp.json()

		if resp.status_code == 422:
			if "errors" in body:
				print(body["message"])
				for error, error_res in body["errors"].items():
					print("{} : {}".format(error, error_res))
			return
		if resp.status_code == 401:
			print(
				"Unauthorized, please add an authorization token with the command set-token to perform this command. \n\nTokens can be created on accounts.plusclouds.com")
			return
		if resp.status_code < 300:
			func(*args, **kwargs)
		else:
			print("Unable to parse the response.")

	return check_status_code
