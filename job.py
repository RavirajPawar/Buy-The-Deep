import requests
import json
import time
from constants import (
    COIN_METADATA,
    HISTORICAL_DATA_API,
    CURRENT_COIN_DATA,
    MAX_DAYS,
    WINDOW_OF_DAYS,
)
from utils.data_collector import fetch_coins_data, get_weekly_high_low

coin_ids_list = [coin_meta["id"] for coin_meta in COIN_METADATA]
coin_weekly_high_low_map = dict()
coin_ids = ",".join(coin_ids_list)
current_price = requests.get(CURRENT_COIN_DATA.format(coin_ids)).json()
historical_data = fetch_coins_data(coin_ids_list)
for id in historical_data:
    coin_weekly_high_low_map[id] = get_weekly_high_low(
        historical_data[id], WINDOW_OF_DAYS
    )
    print(
        "id",
        id,
        "\ntotal weeks",
        len(coin_weekly_high_low_map[id].keys()),
        "\ntotal days",
        len(historical_data[id]),
        "*" * 100,
    )
