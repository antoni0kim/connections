import typer
from . import __version__

app = typer.Typer()


@app.command()
def version():
    """Return version of the connections"""
    print(__version__)


@app.command()
def status():
    """Returns ok on the command line when invoked"""
    print("Status: OK")


if __name__ == "__main__":
    app()
