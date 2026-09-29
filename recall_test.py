import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_BASE_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

print("Searching Hindsight for similar incidents...\n")

result = client.recall(
    bank_id=BANK_ID,
    query="payment API database connection pool exhaustion after deployment"
)

print("RESULT:\n")

print(result)

client.close()