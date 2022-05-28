from multiprocessing import pool
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import time
import matplotlib.dates as mdates
import datetime


def get_weekly_high_low(data, window_of_days=7):
    last_index = len(data)
    sorted_data = list()
    for i in range(0, len(data)):
        if last_index-window_of_days < 0:
            temp = data[:last_index]
            temp = sorted(temp, key=lambda record: record[1])
            temp = sorted(temp, key=lambda record: record[1])
            sorted_data.append(temp[0])
            sorted_data.append(temp[-1])
            break
        else:
            temp = data[last_index-window_of_days:last_index]
            last_index = last_index-window_of_days
        if temp:
            # weekly_low, weekly_high = sorted(temp, key=lambda record: record[1])
            print("weekly data", sorted(temp, key=lambda record: record[1]))
            # sorting asending order of price
            temp = sorted(temp, key=lambda record: record[1])
            sorted_data.append(temp[0])  # weekly low
            sorted_data.append(temp[-1])  # weekly high
    # sorted by date for graph
    return sorted(sorted_data, key=lambda record: record[0])


HISTORICAL_DATA_API = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=USD&days={}"

api_url = HISTORICAL_DATA_API.format("bitcoin", 10000)
api_response = requests.get(api_url)

data = api_response.json()["prices"][:]
data = get_weekly_high_low(data)
x, y = list(), list()

for index, point in enumerate(data, start=1):
    x_point, y_point = point
    # cause time is in milisecond
    x.append(datetime.datetime.fromtimestamp(x_point//1000).date())
    y.append(y_point)
    print(index, " point ", x_point, y_point)

# plt.plot(x,y, color='green', linestyle='dashed', linewidth = 3,
#          marker='X', markerfacecolor='red', markersize=6)

# # naming the x axis
# plt.xlabel('Price')
# # naming the y axis
# plt.ylabel('Time')

# # giving a title to my graph
# plt.title('Uniswap Data')

# function to show the plot
# plt.show()


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.plot(x, y, marker='X', markerfacecolor='red')
plt.gcf().autofmt_xdate()
plt.show()
