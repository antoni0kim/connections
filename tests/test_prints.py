def test_prints_happy(connections_cli, mock_words):
    inputs = " ".join(mock_words)
    result = connections_cli(f"solve {inputs}")
    assert result.exit_code == 0
    lines = result.stdout.strip().split("\n")
    assert len(lines) == 4
