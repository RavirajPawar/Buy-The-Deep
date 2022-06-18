import requests
import json
import time
from constants import (
    COIN_METADATA,
    CURRENT_COIN_DATA,
    WINDOW_OF_DAYS,
)
from utils.data_collector import fetch_coins_data, get_weekly_high_low

coin_ids_list = [coin_meta["id"] for coin_meta in COIN_METADATA]
coin_ids = ",".join(coin_ids_list)
current_price = requests.get(CURRENT_COIN_DATA.format(coin_ids)).json()
historical_data = fetch_coins_data(coin_ids_list)
coin_weekly_high_low_map = {
    id: get_weekly_high_low(historical_data[id][::-1], WINDOW_OF_DAYS)
    for id in historical_data
}
print(coin_weekly_high_low_map["bitcoin"][1])
