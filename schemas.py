tools = [
    {
        "type": "function",
        "function": {
            "name": "customer_history",
            "description": "Retrieve historical customer data including plan type and previous issues using customer ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "Unique identifier of the customer"
                    }
                },
                "required": ["customer_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "knowledge_search",
            "description": "Search the knowledge databased for the issue solution.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_type": {
                        "type": "string",
                        "description": "The type of the issue's product."
                    },
                    "issue_information": {
                        "type": "string",
                        "description": "The keywords describing the problem."
                    },

                },
                "required": ["product_type", "issue_information"]
            }
        }
        
    },
    
]