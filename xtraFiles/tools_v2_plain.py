def get_policy_expiry(policy_number: str):
    """
    Simulates looking up a customer's policy.
    """

    policies = {
        "GIVA-MTR-839213": {
            "expiry_date": "15-Dec-2026",
            "status": "Active"
        },
        "GIVA-MTR-839214": {
            "expiry_date": "10-Aug-2026",
            "status": "Expired"
        }
    }

    return policies.get(
        policy_number,
        {
            "error": "Policy not found"
        }
    )