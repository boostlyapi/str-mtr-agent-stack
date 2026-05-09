import pytest
from pathlib import Path

ROOT = Path(__file__).parent.parent

def test_required_directories_exist():
    required_dirs = [
        "agents",
        "core",
        "docs",
        "tests",
        "data",
    ]

    for directory in required_dirs:
        assert (ROOT / directory).is_dir(), f"Missing required directory: {directory}"

def test_required_files_exist():
    required_files = [
        "requirements.txt",
        "CONTRIBUTING.md",
        "pyproject.toml",
        ".flake8",
        "README.md",
    ]

    for file in required_files:
        assert (ROOT / file).is_file(), f"Missing required file: {file}"

def test_agent_directories_exist():
    required_agent_dirs = [
        "agents/guest-concierge",
    ]

    for directory in required_agent_dirs:
        assert (ROOT / directory).is_dir(), f"Missing required agent directory: {directory}"
