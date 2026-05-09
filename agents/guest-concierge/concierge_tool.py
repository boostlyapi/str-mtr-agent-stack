def generate_concierge_response(guest_question, property_context, local_recommendations, brand_voice=None):
    """
    Generates a deterministic starter response for guest inquiries.
    """
    # Simple deterministic logic for demonstration
    response = f"Thank you for your question about {property_context.get('property_name', 'the property')}. "
    response += "I'm checking our house rules and local guides to give you the best answer."
    
    return {
        "agent_name": "Guest Concierge Agent",
        "status": "success",
        "guest_question": guest_question,
        "response": response,
        "recommendations": local_recommendations[:2] if local_recommendations else [],
        "upsell_opportunities": property_context.get("upsells", []),
        "escalation_required": False
    }
