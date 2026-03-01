from openai import OpenAI
from schemas import tools
import json
from tools import customer_history, knowledge_search, specialist_support, human_support
client = OpenAI()
ticket = input("Enter support ticket: ")

messages = [
    {"role": "system", "content": """
    what you need to do is
    First, Extract key information from the user input unstructure data
    Second, Classify urgentcy level based on the severity of the issue and business impact
    -critical: the issue causing major businees damage financialy, security, and operationally. Immediate action required.
    -high: large number of users affected, but business is still operating. 
    -medium: Partial functionality issue, limited users affected, workaround available.
    -low: Minor issue, feature request, or general inquiry. No business impact risk.
     
    Third, Decide the next best action
    -Use knowledge_search if issue can be resolved automatically.
    -Use customer_history if urgency is high or critical.
    -Escalate to human or specialist if necessary: call customer_history to retrieve context, then provide a structured escalation summary.
    Use available tools when appropriate.

    Rules:
    -If a field is missing, return null.
     
    You must return your final decision strictly in JSON format only.
    Format:
    {
        "urgency": "critical | high | medium | low",
        "next_action": "knowledge_search | customer_history | escalate_specialist | escalate_human",
        "summary": "structured summary of the case"
    }
    Do not include explanations.
    Do not include extra text.
    Return valid JSON only.
    """},
    {"role": "user", "content": ticket}
]

while True:
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        final_response = message.content
        decision = json.loads(final_response)
        
        print(final_response)

        if decision["next_action"] == "escalate_specialist":
            specialist_support(decision["summary"])

        elif decision["next_action"] == "escalate_human":
            human_support(decision["summary"])

        break

    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if tool_name == "knowledge_search":
            tool_result = knowledge_search(
                arguments["product_type"],
                arguments["issue_information"]
            )

        elif tool_name == "customer_history":
            tool_result = customer_history(
                arguments["customer_id"]
            )

        else:
            tool_result = {"error": "Unknown tool"}

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(tool_result)
        })