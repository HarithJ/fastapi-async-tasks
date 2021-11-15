import os
import re

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="compute_heuristic")
def compute_heuristic(transaction_description):
    match = None
    for _ in range(20_000_000):
        match = re.search("Netflix", transaction_description)

    if match:
        merchant_name = "Netflix"
    else:
        merchant_name = "n/a"

    return { "merchant_name": merchant_name }
