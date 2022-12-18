"""Main API file."""

from fastapi import FastAPI, Depends

from back.dependencies import get_token_header
from back.v1 import transactions

app = FastAPI(dependencies=[Depends(get_token_header)])


app.include_router(transactions.router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Hello! I'm ok!"}
