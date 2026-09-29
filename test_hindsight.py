import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

incident = """
INC-021: Payment API production incident.

The payment-api service began returning HTTP 500 errors after deployment v4.1.1.
Error rate reached approximately 35% and database connection pool exhaustion
was observed.

Engineers rolled back deployment v4.1.1 and restarted the payment workers.
Payment processing recovered in approximately 8 minutes.

Root cause: deployment v4.1.1 caused database connection pool exhaustion.
Successful resolution: rollback deployment v4.1.1.
"""

print("1. Storing incident in Hindsight...")

client.retain(
    bank_id=BANK_ID,
    content=incident
)

print("2. Incident stored successfully!")

print("3. Searching Hindsight...")

result = client.recall(
    bank_id=BANK_ID,
    query="Payment API database connection pool exhaustion after deployment"
)

print("\nRelevant memories:\n")

for memory in result.results:
    print("-", memory.text)

client.close()