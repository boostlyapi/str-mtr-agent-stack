import pytest
from agents.guest_concierge.concierge_tool import generate_concierge_response

def test_generate_concierge_response():
    question = "Is there a hot tub?"
    context = {"property_name": "Seaside Cottage", "upsells": ["late checkout"]}
    recommendations = ["Local Pub"]
    
    result = generate_concierge_response(question, context, recommendations)
    
    assert result["status"] == "success"
    assert "Seaside Cottage" in result["response"]
    assert "late checkout" in result["upsell_opportunities"]
    assert "Local Pub" in result["recommendations"]
