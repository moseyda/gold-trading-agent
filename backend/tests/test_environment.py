"""Environment checks that guard the project's mandated runtime."""

import sys
from pathlib import Path

REQUIRED_PYTHON = (3, 11)
BACKEND_DIR = Path(__file__).resolve().parents[1]


def test_python_version_is_3_11() -> None:
    """The project rules mandate Python 3.11."""
    assert sys.version_info[:2] == REQUIRED_PYTHON


def test_env_example_contains_placeholders_only() -> None:
    """The committed environment template must never hold real values."""
    lines = (BACKEND_DIR / ".env.example").read_text(encoding="utf-8").splitlines()
    assignments = [line for line in lines if line.strip() and not line.lstrip().startswith("#")]

    assert assignments, ".env.example should declare at least one variable"
    for line in assignments:
        name, separator, value = line.partition("=")
        assert separator == "=", f"Malformed line: {line!r}"
        assert value.strip() == "", f"{name.strip()} must be an empty placeholder"
