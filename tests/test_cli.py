from unittest import mock

import pytest
from click.testing import CliRunner

from pytest_langchain import main


@pytest.fixture(scope="function")
def runner(request):
    """Fixture for CLI runner."""
    return CliRunner()


def test_cli_help(runner):
    """Tests the help command of Shoeblender CLI."""
    # invoke help command
    result = runner.invoke(main, ["--help"])

    assert not result.exception
    assert "pytest-langchain CLI" in result.output
    assert result.exit_code == 0


def test_cli_run(runner, tmp_path, monkeypatch):
    """Tests pkgviz CLI run."""

    llm_chain = mock.Mock()
    llm_chain.run = mock.Mock(return_value="test")

    monkeypatch.setattr("langchain.chains.load_chain", llm_chain)

    runner.invoke(
        main, ["-c", "tests/test_data/config.yaml", "--openai-api-key", "test"]
    )
