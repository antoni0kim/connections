def test_prints_happy(connections_cli, mock_words):
    result = connections_cli("solve", mock_words)
    assert result.exit_code == 0
    lines = result.stdout.strip().split("\n")
    assert len(lines) == 4
