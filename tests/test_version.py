def test_version(connections_cli):
    """Test the version command."""
    result = connections_cli("version")
    assert result.stdout.strip() == "0.0.1"
