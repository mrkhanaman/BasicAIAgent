import re
from ollama import chat

from tools import get_policy
from tools import TOOLS
from prompts import SYSTEM_PROMPT

print("=== Insurance AI Agent ===")
print("Type 'exit' to quit.\n")

def is_insurance_question(question: str) -> bool:
    """
    Returns True only for insurance-related questions.
    """

    question = question.lower()

    insurance_keywords = [

        "insurance",
        "policy",
        "claim",
        "renew",
        "renewal",
        "coverage",
        "premium",
        "motor",
        "vehicle",
        "accident",
        "expiry",
        "expire",
        "insured"

    ]

    if any(word in question for word in insurance_keywords):
        return True

    policy_pattern = r"[A-Z]{4}-[A-Z]{3}-\d+"

    if re.search(policy_pattern, question.upper()):
        return True

    return False

while True:

    question = input("You: ")
    if question.lower() == "exit":
        break

    if not is_insurance_question(question):

        print()

        print("AI:")

        print(
            "I'm an Insurance AI Assistant and I can only assist with insurance-related queries."
        )

        print()

        continue

    if question.lower() == "exit":
        break

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        tools=TOOLS
    )

    from pprint import pprint

    pprint(response)

#    break