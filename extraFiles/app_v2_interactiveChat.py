from ollama import chat

print("=== AI Assistant ===")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAI:")
    print(response["message"]["content"])
    print()