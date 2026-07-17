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

# Use below code to debug the tool calls and arguments
#    from pprint import pprint
#    pprint(response)
    message = response.message
    tool_calls = message.tool_calls
    if not tool_calls:
        print()
        print("AI:")
        print(message.content)
        print()
        continue
    tool = tool_calls[0]
    function_name = tool.function.name
    arguments = tool.function.arguments
#    print()
#    print("Tool Selected :", function_name)
#    print("Arguments :", arguments)
#    print()

    if function_name == "get_policy":

        policy = get_policy(
            arguments["policy_number"]
        )

#Commenting the Tool Result print statements to avoid cluttering the output 
#        print()
#
#        print("Tool Result:")
#
#        print(policy)

        final_response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": (
                        f"I called the tool get_policy() "
                        f"and received the following result:\n{policy}"
                    )
                },
                {
                    "role": "user",
                    "content": (
                        "Using only the tool result above, "
                        "answer the customer's question professionally. "
                        "If the tool returned an error, explain it politely."
                    )
                }
            ]
        )
        print()

        print("AI:")

        print(final_response.message.content)

        print()

        print()