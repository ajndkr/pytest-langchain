import os
from pathlib import Path

import click
import pytest


@click.command()
@click.option(
    "-c",
    "--config",
    "config_file",
    type=click.Path(exists=True),
    help="Path to config file.",
)
@click.option("--openai-api-key", "openai_api_key", type=str, help="OpenAI API key.")
def main(config_file: str, openai_api_key: str):
    """pytest-langchain CLI"""
    config_file = str(Path(config_file).absolute())
    config_dir = str(Path(config_file).parent)

    os.chdir(Path(__file__).parent)
    pytest.main(
        [
            "--rootdir",
            str(Path(__file__).parent),
            "--langchain-config-dir",
            config_dir,
            "--langchain-config-file",
            config_file,
            "--openai-api-key",
            openai_api_key,
            "tests/",
            "-v",
        ],
        plugins=["langchain"],
    )


if __name__ == "__main__":
    main()
