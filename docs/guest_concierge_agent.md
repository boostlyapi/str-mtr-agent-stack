# Guest Concierge Agent

## Overview
The Guest Concierge Agent is designed to act as a 24/7 digital assistant for STR/MTR guests. It leverages property-specific context and local knowledge to provide helpful, on-brand responses.

## Inputs
*   **Guest Question**: The specific inquiry from the guest.
*   **Property Context**: Amenities, house rules, and unique features.
*   **Local Recommendations**: Curated list of nearby attractions and services.

## Outputs
*   **Response Draft**: A ready-to-send message for the guest.
*   **Upsell Suggestions**: Relevant services (e.g., late checkout) to offer.
*   **Escalation Flag**: Indicates if a human host needs to intervene.

## Example Usage
```python
from agents.guest_concierge.concierge_tool import generate_concierge_response

result = generate_concierge_response(
    "Is there parking available?",
    {"property_name": "Seaside Cottage", "upsells": ["private parking space"]},
    ["Whitby Public Car Park"]
)
```

## Guardrails
*   Never promise amenities not explicitly listed in the property context.
*   Always escalate safety or emergency-related questions.
