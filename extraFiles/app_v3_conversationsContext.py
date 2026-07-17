from ollama import chat

conversation = []

print("=== AI Assistant ===")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message
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

    # Add AI response
    conversation.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nAI:")
    print(answer)
    print()