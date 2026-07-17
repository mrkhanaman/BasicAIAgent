from ollama import chat
from prompts import TOOL_SELECTION_PROMPT, FINAL_RESPONSE_PROMPT


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


def generate_response(question, policy_data):

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": FINAL_RESPONSE_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Customer Question:

{question}

Policy Details:

{policy_data}
"""
            }
        ]
    )

    return response["message"]["content"]