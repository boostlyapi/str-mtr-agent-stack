# Cleaning Schedule Agent

## Purpose
Automate the coordination of cleaning services between guest stays, ensuring properties are always guest-ready and turnover is efficient.

## Workflow
1.  **Monitor Bookings**: Track check-in and check-out dates from the PMS.
2.  **Identify Turnover Windows**: Calculate the time available for cleaning between stays.
3.  **Assign Cleaners**: Match available cleaning staff or services to turnover windows.
4.  **Send Notifications**: Automatically notify cleaners of their schedule and property access details.
5.  **Track Completion**: Monitor and log cleaning completion status.

## Tools
- `booking_monitor_tool.py`: Interfaces with the PMS to track guest movements.
- `turnover_scheduler_tool.py`: Calculates and manages cleaning windows.
- `cleaner_comm_tool.py`: Handles communication with cleaning staff.
