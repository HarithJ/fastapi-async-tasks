from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

from worker import compute_heuristic

class Transaction(BaseModel):
    date: date
    description: str
    amount: str


class Merchant(BaseModel):
    name: str


app = FastAPI()


@app.post("/normalize_merchant")
async def normalize_merchant(tx: Transaction):
    compute_heuristic.delay(tx.description)
    return { "message": "Computing heuristic, this may take a while." }
