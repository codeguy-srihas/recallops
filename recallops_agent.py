import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")


def investigate_incident(incident):
    print("\n🔎 INVESTIGATING INCIDENT...")
    print("=" * 50)

    # 1. Retrieve relevant organizational memory
    recall = client.recall(
        bank_id=BANK_ID,
        query=incident
    )

    print("\n🧠 HISTORICAL MEMORY FOUND")
    print("=" * 50)

    for i, memory in enumerate(recall.results, start=1):
        print(f"\nMemory {i}")
        print(f"Type: {memory.type}")
        print(f"{memory.text}")

    # 2. Ask Hindsight to reason over organizational memory
    reasoning_prompt = f"""
    A new production incident has occurred:

    {incident}

    Use the organization's historical memory to investigate this incident.

    Your task:

    1. Identify the most relevant previous incidents.
    2. Compare their symptoms with the current incident.
    3. Identify what solutions worked previously.
    4. Recommend the most appropriate next action.
    5. Explain the evidence behind the recommendation.
    6. Mention important uncertainty or alternative explanations.

    Do not invent historical incidents or outcomes.
    """

    reflection = client.reflect(
        bank_id=BANK_ID,
        query=reasoning_prompt
    )

    print("\n\n🤖 RECALL OPS RECOMMENDATION")
    print("=" * 50)

    print(reflection.text)

    return reflection


# --------------------------------------------------
# DEMO INCIDENT
# --------------------------------------------------

new_incident = """
INC-028

Service: payment-api
Environment: production
Severity: CRITICAL

The payment-api service is returning HTTP 500 errors.

Error rate: 38%
Latency: 4.8 seconds

Application logs:
- Database connection timeout
- Connection pool exhausted

Deployment v4.1.2 was released approximately 12 minutes
before the incident started.

PostgreSQL is reachable.
Redis is healthy.
"""

investigate_incident(new_incident)

client.close()