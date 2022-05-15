import json
import os

# for file in os.listdir("coin_data"):
#     data = json.load(open(f"coin_data\\{file}", encoding="utf-8"))
#     print(file, data.keys())


data = json.load(open(f"coin_data\\uniswap.json", encoding="utf-8"))


temp = [(i, 2*i) for i in range(1, 11)]
temp = data["prices"][-21:]
# print(temp)
last_index = len(temp)
week_days = 7
for i in range(0, len(temp)):
    print(temp[last_index-week_days:last_index])
    if last_index-week_days < 0:
        print(temp[:last_index])
        print("breaking")
        break
    else:
        last_index = last_index-week_days
