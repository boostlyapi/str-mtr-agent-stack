"""
Boostly Connect: Claude STR/MTR Context Engine
Optimized context injection for property-specific data in Claude.
"""

class ClaudeSTRMTRContext:
    def __init__(self, property_data):
        self.property_data = property_data

    def generate_system_prompt(self, agent_type):
        """
        Generate a highly personalized system prompt for Claude based on property-specific data.
        """
        base_prompt = f"You are the {agent_type} for {self.property_data['name']}. "
        context = f"Property Context: {self.property_data['house_rules']} {self.property_data['local_context']}"
        return base_prompt + context

    def inject_guest_context(self, guest_data):
        """
        Inject guest-specific preferences and history into the conversation context.
        """
        return f"Guest Context: {guest_data.get('preferences', 'No specific preferences recorded.')}"
