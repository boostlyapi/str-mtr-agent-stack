# GitHub Actions Setup (STR/MTR)

## Overview
The STR/MTR Agent Stack includes starter GitHub Actions for testing and linting.

## Status
*   **Workflows**: Starter workflows are provided in `docs/workflows/`.
*   **Manual Setup**: Due to permission constraints, these must be manually added to the `.github/workflows/` directory of the repository.
*   **No Secrets Required**: The current starter workflows do not require any external API keys or secrets.

## Production Readiness
Production schedules and automated reporting should only be enabled once live PMS and AI credentials are securely connected via GitHub Secrets.
