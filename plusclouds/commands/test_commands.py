from plusclouds import cli
import typer


@cli.app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")
