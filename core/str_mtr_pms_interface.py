"""
Boostly Connect: STR/MTR PMS Interface
Specialized abstraction layer for STR/MTR-focused PMS platforms (Hostaway, Guesty, OwnerRez).
"""

class STRMTRPMSInterface:
    """Base interface for STR/MTR PMS integrations."""
    def list_reservations(self):
        pass
    def get_guest_preferences(self, guest_id):
        pass
    def get_property_calendar(self, property_id):
        pass
    def get_property_amenities(self, property_id):
        pass
    def get_portfolio_summary(self):
        pass

class MockSTRMTRPMS(STRMTRPMSInterface):
    """Safe mock PMS implementation for STR/MTR testing."""
    
    def list_reservations(self):
        return [
            {
                "reservation_id": "str-demo-001",
                "guest_name": "Jane Smith",
                "property_name": "Seaside Cottage",
                "check_in": "2026-05-10",
                "check_out": "2026-05-14",
                "stay_type": "short_term",
                "status": "confirmed"
            }
        ]

    def get_guest_preferences(self, guest_id):
        return ["walkable restaurants", "pet-friendly activities", "sea views"]

    def get_property_calendar(self, property_id):
        return {"property_id": property_id, "available_dates": ["2026-05-15", "2026-05-16"]}

    def get_property_amenities(self, property_id):
        return ["Wi-Fi", "parking", "sea view", "pet-friendly"]

    def get_portfolio_summary(self):
        return {"total_properties": 5, "active_bookings": 12, "occupancy_rate": "82%"}
