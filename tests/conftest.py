from typer.testing import CliRunner
import pytest

from connections.cli import app

runner = CliRunner()


@pytest.fixture()
def mock_words():
    """Mock words used for testing solve command on the cli"""
    return [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pear",
        "quince",
        "raspberry",
    ]


@pytest.fixture()
def mock_less_words():
    """Mock words used for testing solve command on the cli"""
    return [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pear",
        "quince",
    ]


@pytest.fixture()
def mock_more_words():
    """Mock words used for testing solve command on the cli"""
    return [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "pear",
        "quince",
        "raspberry",
        "raspberry",
    ]


@pytest.fixture()
def connections_cli():
    """Fixture to run Connections CLI and return results"""

    def invoke(commands=""):
        result = runner.invoke(app, commands.split())
        return result

    return invoke
