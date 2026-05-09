# Contributing to the STR/MTR Agent Stack

Thanks for helping improve the Boostly STR/MTR Agent Stack.

## Principles

* Build for short-term and mid-term rental operators.
* Keep outputs practical, clear, and operationally useful.
* Use UK English in documentation and user-facing content.
* Do not commit API keys, tokens, credentials, or guest data.
* Keep starter workflows safe and manually runnable.

## Code style

* Use Python 3.11+.
* Format Python with Black.
* Lint Python with Flake8.
* Use clear docstrings for public functions and classes.
* Add tests for new core utilities and agent tools.

## Tests

Run tests before opening a pull request:

```bash
pip install -r requirements.txt
pytest
```

## Security

Use environment variables or GitHub Secrets for credentials. Never hardcode production keys.
