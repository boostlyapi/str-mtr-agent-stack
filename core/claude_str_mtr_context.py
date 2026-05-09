"""
Boostly Connect: Claude STR/MTR Context Engine
Optimized context injection for property-specific data in Claude.
"""

def build_str_mtr_context(operator_profile):
    """Builds a base context string for an STR/MTR operator."""
    return f"Operator: {operator_profile.get('name', 'Boostly Host')}. Focus: {operator_profile.get('focus', 'Direct Bookings')}."

def inject_amenity_context(base_context, amenities):
    """Injects property amenities into the context."""
    amenity_str = ", ".join(amenities) if amenities else "standard amenities"
    return f"{base_context} Property Amenities: {amenity_str}."

def generate_local_guide_prompt(property_name, location, guest_type):
    """Generates a prompt for creating a local guide."""
    return f"Create a local guide for {property_name} in {location} tailored for a {guest_type}."
