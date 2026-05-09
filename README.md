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

1.  **Explore the Agents**: Browse the `agents/` directory to see the available specialized agents, starting with the **Guest Concierge Agent**.
2.  **Review Core Utilities**: Check `core/` for the STR/MTR PMS interface and Claude context engine.
3.  **Run Tests**: Verify the repository structure and logic:
    ```bash
    pip install -r requirements.txt
    pytest
    ```
4.  **Read the Docs**: Check the `docs/` directory for implementation guides and the STR/MTR Agent Buildout Plan.
5.  **Ask AI**: Use the provided prompts to implement these agents in your own hospitality stack.

## **Automation & Workflows**

Starter GitHub Actions workflows are provided in `docs/workflows/`. Due to repository permissions, these must be manually added to the `.github/workflows/` directory to enable automated testing and reporting.

---
Built by **Boostly** | [boostly.co.uk](https://boostly.co.uk)
