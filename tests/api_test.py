import unittest
from plusclouds.options.options_parser import OptionsParser


class ApiTest(unittest.TestCase):
	option_parser = OptionsParser.get_instance()

	def test_1_try_api(self):
		options = self.option_parser.recommend("")
		self.assertGreaterEqual(len(options), 3, "API Messages are not working")

	def test_2_try_paths(self):

		self.option_parser.advance_in_directory("communicator")
		options = self.option_parser.recommend("")
		self.assertGreaterEqual(len(options), 2, "API Messages are not working")

		self.option_parser.alter_directory(["iaas", "compute-members"])
		options = self.option_parser.recommend("")
		self.assertGreaterEqual(len(options), 3, "API Messages are not working")


