import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

question = """
A new CRITICAL production incident has occurred.

Service: payment-api
Symptoms:
- HTTP 500 errors
- 38% error rate
- 4.8 second latency
- Database connection timeout
- Connection pool exhausted

Context:
- Deployment v4.1.2 was released 12 minutes before the incident.
- PostgreSQL is reachable.
- Redis is healthy.

Using the organization's historical incident memory:

1. Identify the most relevant previous incidents.
2. Compare their symptoms and context with the current incident.
3. Identify which previous resolution is most applicable.
4. Explain why.
5. Recommend the next action for the engineer.
6. Mention uncertainty or evidence that contradicts the recommendation.

Do not invent information that is not present in organizational memory.
"""

print("RECALL + REASONING")
print("==================")

response = client.reflect(
    bank_id=BANK_ID,
    query=question
)

print("\nRECALL OPS RECOMMENDATION")
print("=========================")
print(response.text)

print("\nMEMORIES USED")
print("=============")
print(response.based_on)

client.close()