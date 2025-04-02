from typing import List, Optional
import typer

from . import __version__
from . import api

app = typer.Typer()


@app.command()
def version():
    """Return version of the connections"""
    print(__version__)


@app.command()
def status():
    """Returns ok on the command line when invoked"""
    print("Status: OK")


@app.command()
def solve(
    words: Optional[List[str]] = typer.Argument(None, help="16 words from Connections")
):
    """
    Returns estimated lists of words in group based on the
    input. Based on ML model used to solve the connections.
    Input must be exactly 16 words.
    """
    if words is None:
        typer.echo("Error: There must be inputs after solve command.", err=True)
        raise typer.Exit(code=1)

    if len(words) != 16:
        typer.echo("Error: Input must have 16 words after solve command", err=True)
        raise typer.Exit(code=1)

    line_output = api.solve_model(words)

    for line in line_output:
        typer.echo(" ".join(line))


if __name__ == "__main__":
    app()
