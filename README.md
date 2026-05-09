# Boostly Connect: STR/MTR Agent Stack

This repository contains the specialized AI Agent Stack for **Short-Term Rental (STR)** and **Mid-Term Rental (MTR)** operations. It is built on the **Workflows, Agents, Tools (WAT)** framework and optimized for the unique requirements of the STR/MTR market.

## **Core Philosophy**
*   **Personalization at Scale**: Every agent is designed to understand and respect the unique nuances of individual properties.
*   **Direct Booking First**: All workflows are geared towards reducing OTA dependency and increasing direct booking conversion.
*   **Operational Leverage**: Automating the "jobs that never stop" to free up hosts for high-value growth activities.

## **Repository Structure**
*   `agents/`: Specialized STR/MTR agents (e.g., Guest Concierge, Dynamic Pricing, Cleaning Schedule).
*   `core/`: Domain-specific utility layers for PMS integration and Claude context handling.
*   `docs/`: Comprehensive documentation, implementation guides, and project reports.
*   `tests/`: Automated tests for agent logic and tool functionality.
*   `.github/workflows/`: Automated execution and reporting pipelines.

## **Key Components**
*   **STR/MTR PMS Interface**: A specialized abstraction layer for platforms like Hostaway, Guesty, and OwnerRez.
*   **Claude Context Engine**: Optimized context injection for property-specific data (house rules, local guides, amenities).

## **Getting Started**

The fastest way to get started is using the **Boostly Connect CLI**:

1.  **Initialize the Stack**:
    ```bash
    python boostly_connect.py init --type str-mtr
    ```
2.  **List Available Agents**:
    ```bash
    python boostly_connect.py list
    ```
3.  **Run an Agent**:
    ```bash
    python boostly_connect.py run guest-concierge
    ```

You can also explore the `agents/` directory, review core utilities in `core/`, and run tests manually:
```bash
pip install -r requirements.txt
pytest
```

## **Automation & Workflows**

Starter GitHub Actions workflows are provided in `docs/workflows/`. Due to repository permissions, these must be manually added to the `.github/workflows/` directory to enable automated testing and reporting.

---
Built by **Boostly** | [boostly.co.uk](https://boostly.co.uk)
