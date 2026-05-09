import pytest
from core.str_mtr_pms_interface import MockSTRMTRPMS
from core.claude_str_mtr_context import build_str_mtr_context, inject_amenity_context

def test_mock_pms_list_reservations():
    pms = MockSTRMTRPMS()
    reservations = pms.list_reservations()
    assert isinstance(reservations, list)
    assert len(reservations) > 0
    assert reservations[0]["stay_type"] == "short_term"

def test_context_building():
    profile = {"name": "Mark", "focus": "Direct Bookings"}
    context = build_str_mtr_context(profile)
    assert "Mark" in context
    assert "Direct Bookings" in context

def test_amenity_injection():
    base = "Welcome."
    amenities = ["Wi-Fi", "Pool"]
    context = inject_amenity_context(base, amenities)
    assert "Wi-Fi, Pool" in context
