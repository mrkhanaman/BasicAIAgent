from ollama import chat

from tools import get_policy
from tools import TOOLS

print("=== Insurance AI Agent ===")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        tools=TOOLS
    )

    from pprint import pprint

    pprint(response)

    break