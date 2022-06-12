import requests
import json
import time
from constants import COIN_METADATA, HISTORICAL_DATA_API, CURRENT_COIN_DATA, MAX_DAYS
from utils.data_collector import fetch_coins_data, get_weekly_high_low

coin_ids_list = ["cardano"]
coin_weekly_high_low_map = dict()
coin_ids = ",".join(coin_ids_list)
current_price = requests.get(CURRENT_COIN_DATA.format(coin_ids)).json()
historical_data = fetch_coins_data(coin_ids_list)
for id in historical_data:
    coin_weekly_high_low_map[id] = get_weekly_high_low(historical_data[id])
