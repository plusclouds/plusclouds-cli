from plusclouds.util.token_util import token_id


def get_key(obj: dict, key: str) -> str:
	try:
		return obj[key]
	except KeyError as e:
		return ""


def cache_constructor(cache_dict: dict):
	def cache_decorator(func):

		def callback(*args, **kwargs):

			url = get_key(kwargs,"url")

			url += get_key(kwargs,"query")
			url += get_key(kwargs,"body")

			if url == "":
				url = "_"

				if len(args) > 1:
					url = args[1]

			if url in cache_dict.keys():
				return cache_dict[url]

			resp = func(*args, **kwargs)
			cache_dict[url] = resp

			return resp

		return callback

	return cache_decorator
