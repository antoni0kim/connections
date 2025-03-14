# src/connections/cli.py
import typer
from . import __version__  # Use a relative import to access __version__

app = typer.Typer()


@app.command()
def version():
    """Return version of the connections"""
    print(__version__)


@app.command()
def create():
    print("Creating User")


if __name__ == "__main__":
    app()
