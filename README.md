# Support Ticket Triage Agent
## How to run
1. Install dependencies:
   pip install openai

2. Set your OpenAI API key in powershell:
   export OPENAI_API_KEY=your_key

3. Run:
   python main.py

## Example input 
Customer info: ID 123, Free plan (upgrade attempted), 4 months on free tier, first time
contacting support
Message 1 (3 hours ago):
&quot;My payment failed when I tried to upgrade to Pro. Can you check
what&#39;s wrong?&quot;

Customer info: ID 456,Enterprise plan, Thailand region, 45 seats, 8 months customer, first
critical issue
Message 1 (2 hours ago):
&quot;ระบบเข้าไม่ได้ครับ ขึ้น error 500&quot;

## Architecture decisions and why
User input > LLM analyse > Use the tools if it needed > JSON format > External action(escalate to human or FAQ)
User input:
   The system accepts raw, unstructured support tickets via console input. This allows flexibility and avoids rigid input formatting constraints.
LLM analyse:
   because it can understand unstructured language better than rule-based logic. This enables contextual reasoning rather than simple keyword detection. 
Tools
   the LLM cannot directly access internal databases or live systems. Functions like knowledge_search() and customer_history() provide structured data to support accurate decision-making.
JSON format
   It ensures consistent, machine-readable output, enabling the backend to reliably interpret and execute actions without ambiguity or format-related errors.
External action
   The backend performs the final action (FAQ response or escalation) based on the JSON decision.

## What could go wrong and how you&#39;d handle it
Classify incorrectly: 
   The model might classify the urgency incorrectly because LLMs have limitations, especially if the user input is unclear or missing context. To handle this, I could add another validation step, such as using a second model to double-check the result, splitting the task into smaller steps (first extract information, then classify), or adding some rule-based logic for critical cases.
   In the long term, it might be better to train our own classification model using our historical data, since it would be more focused on our specific business patterns. In that case, I would use the LLM mainly for extracting keywords and structured information, and let our internal model handle the final urgency classification for better accuracy and consistency. 

## How you&#39;d evaluate this agent in production
In my opinion, this design is usable for production at an early stage, but it still has several weaknesses that could lead to errors and potentially affect the company’s reputation. Because it relies on limited data and general-purpose models, the accuracy and consistency may not be strong enough for high-risk scenarios.
To properly evaluate it, I would monitor classification accuracy, escalation correctness, resolution success rate, and failure cases over time. Based on those results, the system would need continuous refinement—improving prompts, adding validation layers, increasing domain-specific data, or introducing a dedicated internal model—to make it reliable enough for full production use.