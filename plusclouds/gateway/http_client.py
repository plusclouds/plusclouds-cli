import requests

from plusclouds.settings import plusclouds_url
from requests import Request


class HttpGateway:
    def __init__(self, base_url: str = plusclouds_url):
        self.base_url = base_url

    def options(self, url: str = "") -> requests.Response:
        return requests.request("OPTIONS", self.base_url + url)

