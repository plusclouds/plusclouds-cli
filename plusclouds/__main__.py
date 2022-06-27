from plusclouds import cli, __app_name__
import plusclouds.commands.test_commands


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()

