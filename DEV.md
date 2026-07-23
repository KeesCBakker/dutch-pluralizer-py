# Local Development

## Stack

- <a href="https://code.visualstudio.com/">Visual Studio Code</a> with <a href="https://code.visualstudio.com/docs/devcontainers/containers">Dev Containers</a>
- Python 3.14 (via devcontainer)

## Quick start

### Using the devcontainer (recommended)

1. Open the project in Visual Studio Code.
2. When prompted, click **Reopen in Container**. The devcontainer will build automatically with all dependencies installed.
3. Run tests: `python -m pytest`

### Manual setup

1. Make sure you have **libhunspell** installed:
   - **Debian/Ubuntu:** `sudo apt-get install libhunspell-dev`
   - **macOS:** `brew install hunspell`
   - **Windows:** Use WSL or install a pre-built binary.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\Activate` (Windows) or `source venv/bin/activate` (Linux/macOS)
4. Install dependencies: `pip install -r requirements-dev.txt`
5. Install the package in editable mode: `pip install -e .`
6. Run tests: `python -m pytest`

## Testing

- Run all tests: `python -m pytest`
- Run tests matching a keyword: `python -m pytest -k um` (add `-vv` for detail)
- Test files must be prefixed with `test_`.

## Publishing

```bash
# 1. run tests
python -m pytest

# 2. bump version
bumpversion patch

# 3. build
python -m build
twine check dist/*

# 4. upload to PyPI
twine upload dist/*
```
