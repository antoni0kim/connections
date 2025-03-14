
import typer
from . import __version__

app = typer.Typer()


@app.command()
def version():
    """Return version of the connections"""
    print(__version__)


if __name__ == "__main__":
    app()
