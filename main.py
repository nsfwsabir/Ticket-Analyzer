from schemas import TicketAnalysis
from llm import analyze_ticket

message = """
I've been charged twice for my subscription.
Nobody from support is responding.
I need my money back immediately!
"""

result= analyze_ticket(message)

print(result)
print(type(result))

print("\nJSON Output:")
print(result.model_dump_json(indent=2))
