import json
arr = json.load(open("response_1652523345460.json"))
print(arr["prices"][0])
print(len(arr["prices"]))
