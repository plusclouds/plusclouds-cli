import requests

from plusclouds.settings import plusclouds_url
from plusclouds.util.token_util import get_token
from plusclouds.gateway.http_cache import cache_constructor

get_dict = {}
get_cache = cache_constructor(get_dict)

post_dict = {}
post_cache = cache_constructor(post_dict)

delete_dict = {}
delete_cache = cache_constructor(delete_dict)

options_dict = {}
options_cache = cache_constructor(options_dict)


class HttpGateway:
	def __init__(self, base_url: str = plusclouds_url):
		self.base_url = base_url
		self.token, self.has_token = get_token()
		self.latest_request = None
		self.option_request = None

	@get_cache
	def get(self, url: str = "", query=None) -> requests.Response:
		if query is None:
			query = {}
		else:
			get_dict.clear()

		full_url = plusclouds_url + url
		self.latest_request = requests.get(full_url, params=query,
										   headers={"Authorization": "Bearer " + self.token.strip()})
		return self.latest_request

	@post_cache
	def post(self, url: str = "", body=None) -> requests.Response:
		if body is None:
			body = {}
		post_dict.clear()
		full_url = plusclouds_url + url
		self.latest_request = requests.post(full_url, data=body,
											headers={"Authorization": "Bearer " + self.token.strip()})
		return self.latest_request

	@options_cache
	def options(self, url: str = "") -> requests.Response:
		self.option_request = requests.request("OPTIONS", self.base_url + url)

		return self.option_request
