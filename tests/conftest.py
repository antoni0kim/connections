from typer.testing import CliRunner
import pytest

from connections.cli import app

runner = CliRunner()


@pytest.fixture()
def connections_cli():
    """Fixture to run Connections CLI and return results"""

    def invoke(commands=""):
        result = runner.invoke(app, commands.split())
        return result

    return invoke
