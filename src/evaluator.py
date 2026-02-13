evaluation_questions = [
    ("How do I request a refund?", "answerable"),
    ("Can I cancel after shipping?", "partial"),
    ("Do you offer insurance?", "unanswerable"),
    ("How long is delivery?", "answerable"),
]

def evaluate(answer):

    if "not available" in answer.lower():
        return "⚠️ Properly handled unanswerable"

    if len(answer) > 20:
        return "✅ Good Answer"

    return "❌ Weak"
