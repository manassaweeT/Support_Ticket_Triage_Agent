
def human_support(ticket_summary):
    print("Escalating to human...")
    # Save to DB
    # Generate ticket
    # Assign support staff
    return {"status": "escalated"}

def specialist_support(ticket_summary):
    print("Escalating to specialist...")
    # Save to DB
    # Generate ticket
    # Assign support engineer
    return {"status": "escalated"}

def customer_history(customer_id):
    mock_db = {
        "123": {
            "plan": "Free",
            "duration": "4 months",
            "support_history": "First time contacting support"
        },
        "456": {
            "plan": "Enterprise",
            "duration": "8 months",
            "support_history": "First time contacting support"
            
        },
        "789": {
            "plan": "Pro",
            "duration": "5 months",
            "support_history": "First time contacting support"
        }
    }
    return mock_db.get(customer_id, {"message": "No history found"})

def knowledge_search(product_type, issue_information):
    faq = {
        "payment": {
            "default_route": "human_support",
            "issues": {
                "payment failed": {
                    "solution": "Retry payment or check card details.",
                    "route": "self_service"
                },
                "fraud suspected": {
                    "solution": None,
                    "route": "human_support"
                }
            }
        },
        "system": {
            "default_route": "technical_specialist",
            "issues": {
                "505 error": {
                    "solution": "Restart the server and check logs.",
                    "route": "self_service"
                },
                "database corrupt": {
                    "solution": None,
                    "route": "specialist_support"
                }
            }
        }
    }
    product_type = product_type.lower()
    issue_information = issue_information.lower()

    if product_type not in faq:
        return {"solution": None, "route": "human_support"}

    product_data = faq[product_type]
    for keyword, data in product_data["issues"].items():
        if keyword in issue_information:
            return data
    return {
        "solution": None,
        "route": product_data["default_route"]
    }

