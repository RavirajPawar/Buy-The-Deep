"""
Script for store data in json file
Author :- Raviraj Pawar
Date :- 14-5-2022
"""
import concurrent.futures
import requests
from typing import List
from logger import logger
from constants import COIN_METADATA, HISTORICAL_DATA_API, CURRENT_COIN_DATA, MAX_DAYS


def get_data(coin_id):
    try:
        logger.info(f"started {coin_id} api call".center(50, "*"))
        api_url = HISTORICAL_DATA_API.format(coin_id, MAX_DAYS)
        api_response = requests.get(api_url).json()
        return (coin_id, api_response["prices"])
    except Exception as e:
        return (coin_id, f"Exception: {str(e)}")


def fetch_coins_data(coin_ids: List):
    """
    Executes multi-threaded API calls for getting historical data of coin.
    Helper function:    `get_data`

    Args:
        `coin_ids` (list): list of string | ids are assigned by coingecko

    Returns:
        coins_data (dict):
            key (str)     `id`
            value (list)  `historical data`
    """
    coins_data = dict()
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        future_to_url = [
            executor.submit(
                get_data,
                coin_id,
            )
            for coin_id in coin_ids
        ]
        for future in concurrent.futures.as_completed(future_to_url):
            coin_id, coin_data = future.result()
            coins_data[coin_id] = coin_data
    return coin_data
