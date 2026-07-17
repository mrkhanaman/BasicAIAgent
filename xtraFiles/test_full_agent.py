import json

from agent import choose_tool, generate_response
from tools import get_policy

question = "When does policy GIVA-MTR-1234567 expire?"

# Step 1 - AI decides
decision = choose_tool(question)

print("Decision:")
print(decision)

import json

try:
    decision_json = json.loads(decision)

except json.JSONDecodeError:
    print("\nInvalid JSON returned by LLM:")
    print(decision)
    exit()

# Step 2 - Execute tool
if decision_json["tool"] == "get_policy":

    policy = get_policy(
        decision_json["policy_number"]
    )

    print("\nTool Result:")
    print(policy)

    # Step 3 - AI explains
    answer = generate_response(
        question,
        policy
    )

    print("\nFinal Response:")
    print(answer)

else:

    print("No tool required.")