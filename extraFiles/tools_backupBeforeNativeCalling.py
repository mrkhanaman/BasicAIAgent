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