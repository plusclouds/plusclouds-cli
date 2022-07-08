from plusclouds.gateway.http_client import HttpGateway
import string


class OptionsParser:
    def __init__(self):
        self.current_directory = []
        self.gateway = HttpGateway()

        self.latest_response = self.gateway.options("").json()

    def __join_url(self) -> str:
        separator = "/"

        return separator.join(self.current_directory)

    def advance_in_directory(self, path: str = ""):
        if path not in self.latest_response["directories"]:
            raise Exception("The path specified does not exists! Please choose another path.")

        if path != "":
            self.current_directory.append(path)



            self.latest_response = self.gateway.options("/"+self.__join_url()).json()

        return self.latest_response["directories"]

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

        for val in self.latest_response["directories"]:
            if val.startswith(value, 0, len(value)):
                potential_values.append(val)

        return potential_values



