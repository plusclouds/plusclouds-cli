from plusclouds.gateway.http_client import HttpGateway



class OptionsParser:
	__instance = None

	@staticmethod
	def get_instance() -> __instance:
		""" Static access method. """
		if OptionsParser.__instance == None:
			OptionsParser()
		return OptionsParser.__instance

	def __init__(self):

		if OptionsParser.__instance != None:
			raise Exception("This class is a singleton!")

		self.response_cache = {}

		self.current_directory = []
		self.gateway = HttpGateway()

		self.latest_response = self.gateway.options("").json()

		OptionsParser.__instance = self

	def get_latest_response(self):

		def __join_url(self) -> str:
			separator = "/"

			return separator.join(self.current_directory)

	def __get_response(self):

		if self.__join_url() not in self.response_cache.keys():
			self.latest_response = self.gateway.options(self.__join_url()).json()
			self.response_cache[self.__join_url()] = self.latest_response

		self.latest_response = self.response_cache.get(self.__join_url())

	def advance_in_directory(self, path: str = ""):
		self.__get_response()
		if path not in self.latest_response["directories"]:
			raise Exception("The path specified ( {} ) does not exists! Please choose another path.".format(path))

		if path != "":
			if path not in self.current_directory:
				self.current_directory.append(path)

				self.latest_response = self.gateway.options("/" + self.__join_url()).json()

		return self.latest_response["directories"]

	def alter_directory(self, path_list: list):
		if path_list != self.current_directory:

			while True:
				try:
					self.reverse_in_directory()
				except Exception as e:
					break
			for path in path_list:
				self.__get_response()
				self.advance_in_directory(path)

			self.__get_response()

	def reverse_in_directory(self):
		if len(self.current_directory) == 0:
			raise Exception("Cannot reverse, there is no Path configured")
		self.current_directory.pop()

	def method_requirements(self, method):
		if "methods" not in self.latest_response.keys() or method not in self.latest_response["methods"].keys():
			raise Exception("Method does not exists in this path")

		return self.latest_response["methods"][method]

	def recommend(self, value) -> list:
		potential_values = []

		if len(self.current_directory) <= 1:
			pass

		for val in self.latest_response["directories"]:
			if val.startswith(value, 0, len(value)):
				potential_values.append(val)

		return potential_values


if __name__ == "__main__":
	a = OptionsParser()
	a.advance_in_directory("communicator")
	print(a.recommend(""))
	print(a.alter_directory(["iaas", "compute-members"]))

	print(a.recommend(""))
