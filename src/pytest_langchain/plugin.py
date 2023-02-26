"""Custom pytest plugin for pytest-langchain."""


def pytest_addoption(parser):
    parser.addoption(
        "--langchain-config-dir",
        action="store",
        help="path to config directory",
    )
    parser.addoption(
        "--langchain-config-file",
        action="store",
        help="path to config YAML file",
    )
    parser.addoption(
        "--openai-api-key",
        action="store",
        help="OpenAI API key",
    )
