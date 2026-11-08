from schemas import TicketAnalysis
from llm import analyze_ticket

test_messages = [
    "I was charged twice for my subscription.",

    "My application crashes every time I open it.",

    "I love your product! The new update is amazing."
]

for message in test_messages:
    result = analyze_ticket(message)
    print(result.model_dump_json(indent=2))
