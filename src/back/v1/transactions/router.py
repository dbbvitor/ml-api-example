"""Defines the route and methods to the recommend logic."""

from datetime import date
from fastapi import APIRouter

from back.v1.transactions import logic
from back.v1.transactions.models import RequestResponse

router = APIRouter()


@router.get("/transactions/", tags=["transactions"], response_model=list[RequestResponse])
async def read_random_transaction(input_date: date, request_id: str) -> list[dict]:
    """
    Responds to the user random transaction request.

    Args:
        request_id: the id of the request for logging purposes.
        input_date: date of the transaction.

    Returns:
        response: response containing transactions and flags.
    """
    transaction = logic.bitcoin_data_loader(input_date=input_date, request_id=request_id)
    control = logic.control_flagger()

    return [{"request_id": request_id, "transaction": transaction, "control": control}]
