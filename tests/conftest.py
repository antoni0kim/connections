from typer.testing import CliRunner
import connections
import shlex
import pytest

runner = CliRunner()


@pytest.fixture()
def connections_cli():
    """Fixture to run Connections CLI and return results"""
    def invoke(commands=""):
        options = shlex.split(commands) if commands else []
        result = runner.invoke(connections.cli.app, options)
        if result.exit_code != 0:
            pytest.fail(
                f"CLI command failed: {result.exit_code}, {result.stderr}")

            return result

    return invoke
