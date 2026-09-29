import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")


def resolve_incident():

    print("\n🚨 INCIDENT INC-028")
    print("=" * 50)

    print("""
Service: payment-api
Severity: CRITICAL
Error rate: 38%
Latency: 4.8 seconds

Symptoms:
- HTTP 500
- Database connection timeout
- Connection pool exhausted

Recent deployment:
v4.1.2
""")

    print("\n🤖 RECALL OPS RECOMMENDATION")
    print("=" * 50)

    print("""
Recommended action:

ROLLBACK deployment v4.1.2

Reason:
A previous payment-api incident (INC-021) had
the same connection-pool exhaustion pattern
immediately after deployment.

The rollback successfully restored service.
""")

    approval = input("\nApprove rollback? (yes/no): ")

    if approval.lower() != "yes":
        print("\n❌ Rollback cancelled.")
        print("Engineer remains in control.")
        return

    print("\n✅ Rollback approved by engineer.")

    # Simulate remediation
    print("\n⚙️ Rolling back v4.1.2...")

    print("Deployment rolled back.")
    print("Restarting payment workers...")

    resolution_time = 7.7

    print(f"\n🟢 INCIDENT RESOLVED")
    print(f"Resolution time: {resolution_time} minutes")

    # Store the new organizational learning
    outcome = f"""
    INC-028: Payment API production incident.

    Service: payment-api
    Deployment: v4.1.2

    Symptoms:
    HTTP 500 errors, database connection timeout,
    connection pool exhaustion.

    Investigation:
    The incident occurred approximately 12 minutes
    after deployment v4.1.2.

    Historical reference:
    INC-021 showed a highly similar failure pattern
    after deployment v4.1.1.

    Action taken:
    Engineer approved rollback of deployment v4.1.2
    and restart of payment workers.

    Outcome:
    Incident resolved successfully in {resolution_time} minutes.

    Organizational lesson:
    When payment-api experiences HTTP 500 errors and
    database connection pool exhaustion shortly after
    deployment, a deployment rollback should be considered
    after confirming the incident pattern.

    Important:
    The rollback was approved by a human engineer.
    """

    print("\n🧠 Updating organizational memory...")

    client.retain(
        bank_id=BANK_ID,
        content=outcome
    )

    print("✅ New experience stored in Hindsight.")
    print("\nRecallOps has learned from INC-028.")


resolve_incident()

client.close()