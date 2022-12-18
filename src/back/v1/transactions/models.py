"""Data input/output validation."""
from typing import Any

from pydantic import BaseModel


class RequestResponse(BaseModel):
    """Template for the request responses."""
    request_id: str
    transaction: Any
    control: bool
