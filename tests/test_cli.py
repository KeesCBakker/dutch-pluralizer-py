import subprocess
import sys
import pytest

from dutch_pluralizer.speller import new_hunspell_nl

_hunspell_available = True
try:
    new_hunspell_nl()
except (ImportError, OSError):
    _hunspell_available = False


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "-m", "dutch_pluralizer", *args],
        capture_output=True, text=True
    )
    return result


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_pluralize():
    result = run_cli("-p", "kaas")
    assert result.returncode == 0
    assert result.stdout.strip() == "kazen"


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_singularize():
    result = run_cli("-s", "kazen")
    assert result.returncode == 0
    assert result.stdout.strip() == "kaas"


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_default_pluralize():
    result = run_cli("kaas")
    assert result.returncode == 0
    assert result.stdout.strip() == "kazen"


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_verbose_no_result():
    result = run_cli("-v", "-p", "xyzzy")
    assert result.returncode == 0
    assert "Could not pluralize" in result.stdout


def test_cli_help():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "positional arguments:" in result.stdout
    assert "--pluralize" in result.stdout
    assert "--singularize" in result.stdout
