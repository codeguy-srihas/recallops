import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

new_incident = """
NEW INCIDENT: INC-029

Service: payment-api
Environment: production
Severity: CRITICAL

The payment-api service is returning HTTP 500 errors.
Error rate is approximately 34%.
Latency has increased to approximately 4.2 seconds.

Application logs show:
- Database connection timeout
- Connection pool exhausted

Deployment v4.1.3 was released approximately 15 minutes before
the incident started.

The database is reachable and Redis is healthy.
"""

print("NEW INCIDENT")
print("====================")
print(new_incident)

print("\nSearching organizational memory...\n")

result = client.recall(
    bank_id=BANK_ID,
    query="""
    Find previous production incidents similar to this new incident.

    Service: payment-api
    Symptoms: HTTP 500, database connection timeout,
    connection pool exhaustion
    Context: recent deployment
    """

)

print("HINDSIGHT FOUND:")
print("====================")

for i, memory in enumerate(result.results, start=1):
    print(f"\n--- Memory {i} ---")
    print("Type:", memory.type)
    print("Text:", memory.text)

client.close()