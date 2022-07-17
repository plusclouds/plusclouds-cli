def cache_constructor(cache_dict: dict):
	def cache_decorator(func):

		def callback(*args, **kwargs):
			url = kwargs.get("url", "")
			if url == "":
				url = "_"

				if len(args) > 1:
					url = args[1]

			if url in cache_dict.keys():
				print("returning cached dir")
				return cache_dict[url]

			resp = func(*args, **kwargs)
			cache_dict[url] = resp
			print("new cache on {}".format(url))

			return resp

		return callback

	return cache_decorator
