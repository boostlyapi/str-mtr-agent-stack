# Dynamic Pricing Agent

## Purpose
Optimise rental rates based on market demand, occupancy, and local events to maximise revenue and occupancy for STR/MTR properties.

## Workflow
1.  **Fetch Market Data**: Retrieve current market rates for similar properties in the local area.
2.  **Analyze Occupancy**: Check current and historical occupancy rates for the property.
3.  **Identify Events**: Scan local event calendars for upcoming festivals, conferences, or holidays.
4.  **Calculate Optimal Rate**: Use AI to synthesize data and recommend the optimal daily rate.
5.  **Generate Report**: Provide a pricing recommendation report with justifications.

## Tools
- `market_data_tool.py`: Fetches competitor pricing and market trends.
- `occupancy_analyzer_tool.py`: Analyzes property-specific occupancy data.
- `event_scout_tool.py`: Identifies local events impacting demand.
