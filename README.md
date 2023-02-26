# 🦜️🔗✅ pytest-langchain

Pytest-style test runner for langchain projects.

<div align="center">

[![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/ajndkr/pytest-langchain/dot/blob/main/LICENSE)
[![CI](https://github.com/ajndkr/pytest-langchain/actions/workflows/ci.yaml/badge.svg)](https://github.com/ajndkr/pytest-langchain/actions/workflows/ci.yaml)
[![Publish](https://github.com/ajndkr/pytest-langchain/actions/workflows/publish.yaml/badge.svg)](https://github.com/ajndkr/pytest-langchain/actions/workflows/publish.yaml)

</div>

## Installation

### Install from PyPI:

```
pip install pytest-langchain
```

### Install from source:

```
git clone https://github.com/ajndkr/pytest-langchain
cd pytest-langchain
pip install .
```

## Usage

-   Serialise your LLM chain into a YAML file.
    Refer to [docs](https://langchain.readthedocs.io/en/latest/modules/chains/generic/serialization.html)
    for more details.

-   Create a new configuration YAML file to run `pytest-langchain` with the following structure:

    ```yaml
    chain_file: <path to chain YAML file>
    test_cases:
    - [<input-1>, <expected output-1>]
    - [<input-2>, <expected output-2>]
    - ...
    ```

-   Run `pytest-langchain`:

    ```
    pytest-langchain -c <path to config YAML file> --openai-api-key <OPENAI API key>
    ```

    For more options, run `pytest-langchain --help`.
