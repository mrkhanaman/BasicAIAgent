from ollama import chat

conversation = [
    {
        "role": "system",
        "content": """
You are an Insurance Customer Support Assistant.

Rules:

1. Answer only insurance-related questions.
2. Keep answers short and professional.
3. If you don't know an answer, say you don't know.
4. Never make up policy details.
5. Be polite and helpful.
"""
    }
]

print("=== AI Assistant ===")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    conversation.append(
        {
            "role": "user",
            "content": question
        }
    )

    response = chat(
        model="llama3.2:3b",
        messages=conversation
    )

    answer = response["message"]["content"]

    conversation.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nAI:")
    print(answer)
    print()