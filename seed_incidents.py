import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

incidents = [

    """
    INC-014: Payment API database overload.

    Service: payment-api
    Environment: production
    Severity: HIGH

    The payment-api service experienced severe latency and intermittent
    HTTP 500 errors. Database CPU usage reached approximately 95%.
    There was no recent application deployment before the incident.

    Investigation showed that a sudden increase in database queries caused
    database resource exhaustion.

    Root cause: PostgreSQL database overload.

    Resolution: Engineers restarted the database and temporarily reduced
    expensive background queries.

    The service recovered in approximately 14 minutes.

    Lesson: When payment-api has high latency without a recent deployment,
    check database CPU and query load before investigating application
    deployments.
    """,

    """
    INC-009: Order API connection pool exhaustion.

    Service: order-api
    Environment: production
    Severity: HIGH

    The order-api service began returning HTTP 500 errors.
    Application logs showed database connection pool exhaustion.

    There was no recent deployment.

    Investigation showed that the connection pool limit was too low
    for the current traffic level.

    Root cause: Insufficient database connection pool capacity.

    Resolution: Engineers increased the database connection pool size.

    The service recovered in approximately 11 minutes.

    Lesson: Connection pool exhaustion without a recent deployment can
    indicate insufficient pool capacity. Check pool utilization and limits.
    """,

    """
    INC-018: Payment API cache failure after deployment.

    Service: payment-api
    Environment: production
    Severity: HIGH

    The payment-api service experienced elevated latency and HTTP 500 errors
    approximately 10 minutes after deployment v4.0.8.

    Database metrics remained normal, but Redis connection errors increased.

    Investigation showed that the new deployment contained an incompatible
    Redis connection configuration.

    Root cause: Incorrect Redis configuration introduced by deployment v4.0.8.

    Resolution: Engineers rolled back deployment v4.0.8.

    Payment processing recovered in approximately 6 minutes.

    Lesson: When payment-api failures occur shortly after deployment,
    compare the deployment changes with recent infrastructure and dependency
    configuration changes.
    """
]

for i, incident in enumerate(incidents, start=1):
    print(f"Storing historical incident {i}/{len(incidents)}...")

    client.retain(
        bank_id=BANK_ID,
        content=incident
    )

    print("Stored successfully.\n")

client.close()

print("================================")
print("Historical incidents seeded!")
print("================================")