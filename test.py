from multiprocessing import pool
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import time
import matplotlib.dates as mdates
import datetime


def get_weekly_high_low(data, window_of_days=7):
    weekly_high_low_data = dict()
    for i in range(0, len(data), window_of_days):
        # item of weekly_data is list where 0th index is timestamp 1st index is price in $
        weekly_data = data[i: i+window_of_days]
        # sorting weekly_data in ascending order with help of price
        weekly_data = sorted(weekly_data, key=lambda dayly_data: dayly_data[1])
        weekly_high_low_data[i+1] = (weekly_data[-1], weekly_data[0])
        print("week", i+1, (weekly_data[-1], weekly_data[0]))


HISTORICAL_DATA_API = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=inr&days={}"

api_url = HISTORICAL_DATA_API.format("uniswap", 10000)
api_response = requests.get(api_url)

# reversing data for making weekly high low batch
data = api_response.json()["prices"][:]
get_weekly_high_low(data[::-1])
