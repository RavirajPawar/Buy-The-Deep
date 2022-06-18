"""
Author :- Raviraj Pawar
Date :- 14-5-2022
"""
import concurrent.futures
import requests
from typing import List
from logger import logger
from constants import (
    COIN_METADATA,
    HISTORICAL_DATA_API,
    CURRENT_COIN_DATA,
    MAX_DAYS,
    WINDOW_OF_DAYS,
)
from utils import calculate_time


def get_data(coin_id):
    """
    Makes coingecko api call and extracts 'price' key which has historical data.
    other keys in response `market_caps` and `total_volumes`.

    Args:
        coint_id (str): id assigned by coingecko 'coins/list' api

    Returns:
        After getting response returns tuple
        index 0 (str):  coin_id
        index 1 (list): historical data
    """
    try:
        logger.info(f"started {coin_id} api call".center(50, "*"))
        api_url = HISTORICAL_DATA_API.format(coin_id, MAX_DAYS)
        api_response = requests.get(api_url).json()
        return (coin_id, api_response["prices"])
    except Exception as e:
        return (coin_id, f"Exception: {str(e)}")


@calculate_time
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
    logger.info("Finised extraction of coins historical data")
    return coins_data


def get_weekly_high_low(data, window_of_days):
    """
    Gets historical data of coin, makes batch of 7 days and finds high and low of that week.

    Args:
        data (list of list) : list of historical data each item consist timestamp and price in INR.
        window_of_days (int): constant value 7 for representing week.

    Returns:
        weekly_high_low_data (dict):
            key (int)   : week number from data available
            value(tuple): index 0 for weekly high index 1 for weekly low

    """
    weekly_high_low_data = dict()
    for i in range(0, len(data), window_of_days):
        # item of weekly_data is list where 0th index is timestamp 1st index is price in ₹
        weekly_data = data[i : i + window_of_days]
        # removing null price timestamp from weekly data
        weekly_data = [data for data in weekly_data if data[1]]
        # sorting weekly_data in ascending order with help of price
        weekly_data = sorted(weekly_data, key=lambda dayly_data: dayly_data[1])
        if weekly_data:
            weekly_high_low_data[i + 1] = (weekly_data[-1], weekly_data[0])
    return weekly_high_low_data
