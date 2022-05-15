"""
Script for store data in json file
Author :- Raviraj Pawar
Date :- 14-5-2022
"""
import concurrent.futures
import os
import json
import requests
from logger import logger
import constants as constant


def save_coin_data(coin_details, api_url, max_days):
    """
        Calls coingecko api for historical data and saves response in json format.

        Args:
            coin_details (dict) :- key id is used for calling api
            api_url (str)       :- coingecko historical data api
            max_days            :- how many days data required

        Returns (boolean)       :- On successful execution returns True else False
    """
    try:
        api_url = api_url.format(coin_details['id'], max_days)
        api_response = requests.get(api_url)
        if not os.path.exists("coin_data"):
            os.makedirs("coin_data")

        with open(os.path.join("coin_data", f"{coin_details['id']}.json"), "w+", encoding="utf-8") \
                as file:
            json.dump(api_response.json(), file, ensure_ascii=False)

        logger.info(
            f"coin {coin_details['id']} processed successfully".center(80, "*"))

        return True

    except OSError:
        logger.exception(
            f"Exception occured coin {coin_details['id']}\n",  exc_info=True)
        return False


with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    future_to_url = [executor.submit(
        save_coin_data, coin_details, constant.HISTORICAL_DATA_API, constant.MAX_DAYS)
        for coin_details in constant.COIN_METADATA]
    for future in concurrent.futures.as_completed(future_to_url):
        print(future.result())
