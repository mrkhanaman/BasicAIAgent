from pathlib import Path
import pandas as pd

# Load the CSV only once when the application starts
DATA_FILE = Path(__file__).parent.parent / "data" / "customer_data.csv"

df = pd.read_csv(DATA_FILE)


def get_policy(policy_number: str):
    """
    Returns the policy details for a given policy number.
    """

    result = df[df["policy_number"] == policy_number]

    if result.empty:
        return {
            "error": "Policy not found"
        }

    return result.iloc[0].to_dict()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_policy",
            "description": (
                "Retrieve customer insurance policy details ONLY when "
                "the user explicitly provides a valid insurance policy number. "
                "Examples of policy numbers include GIVA-MTR-839201. "
                "Do NOT call this tool for greetings, casual conversation, "
                "general knowledge questions, or questions that do not contain "
                "a valid insurance policy number."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "policy_number": {
                        "type": "string",
                        "description": "Customer insurance policy number"
                    }
                },
                "required": [
                    "policy_number"
                ]
            }
        }
    }
]