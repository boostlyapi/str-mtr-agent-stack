# House Rules Agent

## Purpose
Ensure guests are aware of and comply with property-specific house rules, reducing disputes and maintaining property standards.

## Workflow
1.  **Ingest House Rules**: Load the specific house rules for the property.
2.  **Communicate Rules**: Send a clear, friendly summary of key rules to guests before check-in.
3.  **Answer Guest Queries**: Use AI to answer guest questions about what is and isn't allowed.
4.  **Monitor Compliance**: (Optional) Integrate with smart home sensors to flag potential rule violations (e.g., noise levels).
5.  **Handle Violations**: Provide templates and guidance for addressing rule violations professionally.

## Tools
- `rules_ingestor_tool.py`: Manages property-specific rule sets.
- `guest_qa_tool.py`: AI-powered interface for answering guest questions about rules.
- `compliance_monitor_tool.py`: (Placeholder) Logic for integrating with monitoring hardware.
