def test_prints_happy(connections_cli, mock_words):
    inputs = " ".join(mock_words)
    result = connections_cli(f"solve {inputs}")
    assert result.exit_code == 0
    lines = result.stdout.strip().split("\n")
    assert len(lines) == 4


def test_prints_empty(connections_cli):
    result = connections_cli("solve ")
    assert result.exit_code == 1


def test_prints_more(connections_cli, mock_more_words):
    inputs = " ".join(mock_more_words)
    result = connections_cli(f"solve {inputs}")
    assert result.exit_code == 1


def test_prints_more(connections_cli, mock_less_words):
    inputs = " ".join(mock_less_words)
    result = connections_cli(f"solve {inputs}")
    assert result.exit_code == 1
