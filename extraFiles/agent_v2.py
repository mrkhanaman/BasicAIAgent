from ollama import chat
from prompts import TOOL_SELECTION_PROMPT


def choose_tool(question):

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": TOOL_SELECTION_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]