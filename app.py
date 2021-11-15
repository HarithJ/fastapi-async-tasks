from datetime import date
import re
import requests
import json

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

class Transaction(BaseModel):
    date: date
    description: str
    amount: str


class Merchant(BaseModel):
    name: str


app = FastAPI()

def normalize_merchant_heuristic(tx: Transaction):
    """
    Please do not focus on the implementation of this heuristic.
    For the purpose of the exercise, we will assume that the heuristic is already
    implemented with the code below. We are looping over the regex on purpose to
    reflect the slowness of a real-world implementation.
    """
    match = None
    for _ in range(20_000_000):
        match = re.search("Netflix", tx.description)

    if match:
        data = { "name": "Netflix" }
    else:
        data = { "name": "n/a" }

    # in reality this would be a env var
    webhook_url = "http://localhost:9898/normalize_merchant_response"
    r = requests.post(
        webhook_url,
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )


@app.post("/normalize_merchant")
async def normalize_merchant(tx: Transaction, background_tasks: BackgroundTasks):
    background_tasks.add_task(normalize_merchant_heuristic, tx)
    return {"message": "Matching heuristic, this may take a while"}


@app.post("/normalize_merchant_response")
def normalize_merchant_response(merchant: Merchant) -> Merchant:
    print(merchant)
    return merchant
