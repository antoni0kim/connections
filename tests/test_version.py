def test_version(connections_cli):
    """Test the version command."""
    result = connections_cli("version")
    assert result.stdout.strip() == "0.0.1"


def test_status(connections_cli):
    """Test the status of the app. Should return OK"""
    result = connections_cli("status")
    assert result.stdout.strip() == "Status: OK"
