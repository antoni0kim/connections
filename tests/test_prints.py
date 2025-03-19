def test_prints_happy(connections_cli, mock_words):
    inputs = " ".join(mock_words)
    result = connections_cli(f"solve {inputs}")
    assert result.exit_code == 0
    lines = result.stdout.strip().split("\n")
    assert len(lines) == 4


def test_prints_empty(connections_cli):
    result = connections_cli("solve ")
    assert result.exit_code == 1
