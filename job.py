import requests
import json
import time
from constants import COIN_METADATA, HISTORICAL_DATA_API, CURRENT_COIN_DATA, MAX_DAYS
from utils.data_collector import fetch_coins_data

coin_ids = ",".join([coin_meta["id"] for coin_meta in COIN_METADATA])

current_price = requests.get(CURRENT_COIN_DATA.format(coin_ids))
print(current_price.json())

fetch_coins_data([coin_meta["id"] for coin_meta in COIN_METADATA])
