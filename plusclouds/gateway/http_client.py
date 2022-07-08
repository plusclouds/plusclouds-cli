import requests

from plusclouds.settings import plusclouds_url
from plusclouds.util.token_util import get_token


class HttpGateway:
	def __init__(self, base_url: str = plusclouds_url):
		self.base_url = base_url
		self.token, self.has_token = get_token()
		self.latest_request = None
		self.option_request = None

	def get(self, url: str = "") -> requests.Response:
		full_url = plusclouds_url + "/" + url
		self.latest_request = requests.get(full_url, headers={"Authorization": "Bearer " + self.token.strip()})
		return self.latest_request

	def post(self, url: str = "", body=None) -> requests.Response:
		if body is None:
			body = {}

		full_url = plusclouds_url + "/" + url
		self.latest_request = requests.post(full_url, data=body,
											headers={"Authorization": "Bearer " + self.token.strip()})
		return self.latest_request

	def options(self, url: str = "") -> requests.Response:
		self.option_request = requests.request("OPTIONS", self.base_url + url)
		return self.option_request
