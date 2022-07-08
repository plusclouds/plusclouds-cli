from plusclouds.options.options_parser import OptionsParser
import readline
from plusclouds.gateway.http_client import HttpGateway

readline.parse_and_bind("tab: complete")


class CLIRecommender:
    def __init__(self):
        self.option_parser = OptionsParser()

    def complete(self, text, state):
        line = readline.get_line_buffer()

        try:
            if len(line) > 0:
                tokens = line.split(" ")
                try:
                    if len(tokens) > 1 or (len(line.strip()) != 0 and line[-1] == " "):
                        self.option_parser.alter_directory(tokens)
                except Exception as e:
                    pass

            try:
                if len(line.strip()) == 0 or line[-1] == " ":
                    return self.option_parser.recommend("")[state]
            except Exception as e:
                pass

            return self.option_parser.recommend(text.strip())[state]
        except Exception as e:
            pass


completer = CLIRecommender()

readline.set_completer(completer.complete)

line = input('PlusClouds> ')

url_paths = line.strip().split(" ")

gateway = HttpGateway()

print(gateway.get("/".join(url_paths)).json())
