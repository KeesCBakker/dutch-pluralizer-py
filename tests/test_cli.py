import subprocess
import sys
import pytest

from dutch_pluralizer.speller import new_hunspell_nl

_hunspell_available = True
try:
    new_hunspell_nl()
except (ImportError, OSError):
    _hunspell_available = False


def run_cli(*args, stdin=None):
    result = subprocess.run(
        [sys.executable, "-m", "dutch_pluralizer", *args],
        input=stdin, capture_output=True, text=True
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


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_pipe():
    result = run_cli(stdin="kaas\nauto\nboek\n")
    assert result.returncode == 0
    assert result.stdout.splitlines() == ["kazen", "auto's", "boeken"]


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_consonant_doubling():
    result = run_cli(stdin="kaas\nhuis\nvoetbal\n")
    assert result.returncode == 0
    assert result.stdout.splitlines() == ["kazen", "huizen", "voetballen"]


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_failed_word_prints_empty_line():
    result = run_cli(stdin="kaas\nxyzzy\n")
    lines = result.stdout.splitlines()
    assert lines[0] == "kazen"
    assert lines[1] == ""


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_empty_line_prints_empty_line():
    result = run_cli(stdin="kaas\n\nauto\n")
    lines = result.stdout.splitlines()
    assert lines[0] == "kazen"
    assert lines[1] == ""
    assert lines[2] == "auto's"


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_singularize():
    result = run_cli("-s", stdin="kazen\nboeken\nhuizen\n")
    assert result.returncode == 0
    assert result.stdout.splitlines() == ["kaas", "boek", "huis"]


@pytest.mark.skipif(not _hunspell_available, reason="libhunspell not available")
def test_cli_stdin_with_word_arg_still_works():
    result = run_cli("kaas", stdin="auto\n")
    assert result.returncode == 0
    assert result.stdout.strip() == "kazen"


def test_cli_help():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "positional arguments:" in result.stdout
    assert "Omit to read from stdin" in result.stdout
    assert "--pluralize" in result.stdout
    assert "--singularize" in result.stdout
