from schemas import TicketAnalysis
from llm import analyze_ticket

test_cases = [
    {
        "message": "I was charged twice for my subscription.",
        "expected_category": "billing",
        "expected_priority": "medium"
    },
    {
        "message": "My app keeps crashing whenever I try to log in.",
        "expected_category": "technical",
        "expected_priority": "medium"
    },
    {
        "message": "I was charged for my subscription even after I cancelled it last week.",
        "expected_category": "billing",
        "expected_priority": "high"
    },
    {
        "message": "I would like to cancel my subscription before the next billing cycle.",
        "expected_category": "billing",
        "expected_priority": "low"
    },
    {
        "message": "The latest update looks great! I really like the new dashboard design.",
        "expected_category": "general",
        "expected_priority": "low"
    }
]

category_correct=0
priority_correct=0
total=len(test_cases)

for index, case in enumerate(test_cases, start=1):

    print(f"\n Test case {index} --")

    try:
        result = analyze_ticket(case["message"])

        category_match=(
            result.category == case['expected_category']
        )

        priority_match=(
            result.priority == case['expected_priority']
        )

        if category_match:
            category_correct+=1
        if priority_match:
            priority_correct+=1

        print(f"Message: {case["message"]}")
        print(f"Predicted category: {result.category}")
        print(f"Expected catogory: {case['expected_category']}")
        print(f"Predicted priority: {result.priority}")
        print(f"Expected priority: {case['expected_priority']}")

        print(f"Category: {'PASS' if category_match else 'FAIL'}")
        print(f"Priority: {'PASS' if priority_match else 'FAIL'}")

    except Exception as e:
        print(f"Test failed: {e}")


category_accuracy=(category_correct/total)*100
priority_accuracy=(priority_correct/total)*100

print("\n EVALUATION SUMMARY ")

print(f"Total Tests: {total}")
print(f"Category Accuracy: {category_accuracy:.2f}%")
print(f"Priority Accuracy: {priority_accuracy:.2f}%")
        