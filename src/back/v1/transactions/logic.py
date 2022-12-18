"""Logic used by the transactions' module/endpoint."""

import logging
from random import random
from datetime import date
from back.utils import s3_connector


def bitcoin_data_loader(input_date: date, request_id: str) -> str:
    """
    Retrieves a random bitcoin transaction on the specified date.

    Args:
        request_id: the id of the request for logging purposes.
        input_date: date of the transaction.

    Returns:
        rand_btc_trans: a bitcoin transaction encoded as a json.
    """
    logging.debug("Initializing bitcoin_data_loader.")

    spark = s3_connector.get_spark()
    date_filter = input_date.strftime("%Y-%m-%d")

    logging.info(f"User requested ({request_id}) transactions on {date_filter}.")

    df = spark.read.parquet(f"s3a://aws-public-blockchain/v1.0/btc/transactions/date={date_filter}").limit(100).rdd
    sample = str(df.takeSample(withReplacement=False, num=1)[0])

    logging.info(f"Returning the following transaction: {sample}")

    return sample


def control_flagger() -> bool:
    """
    Returns a boolean flag randomly.

    Returns:
        control: boolean flag
    """
    return random() < 0.5
