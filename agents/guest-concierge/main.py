from concierge_tool import generate_concierge_response

def main():
    # Safe demo input
    guest_question = "Can I have a late checkout on Sunday?"
    property_context = {
        "property_name": "Seaside Cottage",
        "upsells": ["late checkout", "welcome hamper"]
    }
    local_recommendations = ["Whitby Abbey", "Magpie Cafe"]
    
    result = generate_concierge_response(
        guest_question, 
        property_context, 
        local_recommendations
    )
    
    print(f"Agent: {result['agent_name']}")
    print(f"Question: {result['guest_question']}")
    print(f"Response Draft: {result['response']}")
    print(f"Upsells: {result['upsell_opportunities']}")

if __name__ == "__main__":
    main()
