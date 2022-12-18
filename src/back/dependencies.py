"""Validations for the user requests."""

from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    """
    Authentication placeholder.
    Args:
        x_token: fake authentication token.
    """
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
