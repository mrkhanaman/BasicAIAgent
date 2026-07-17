from ollama import chat

conversation = [
    {
        "role": "system",
        "content": """
You are an AI assistant.

Your job is to identify the user's intent.

Return ONLY JSON.

Available intents:

policy_renewal
policy_expiry
claim_status
coverage_query
greeting
unknown

Return JSON in this format:

{
  "intent": "",
  "confidence": 0.0
}
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
        messages=conversation,
        stream=True
    )

    answer = ""
    print("\nAI: ", end="", flush=True)
    for chunk in response:
        if "message" in chunk and "content" in chunk["message"]:
            content = chunk["message"]["content"]
            answer += content
            print(content, end="", flush=True)
    print("\n")

    conversation.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nAI:")
    print(answer)
    print()