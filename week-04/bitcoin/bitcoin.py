# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
# Practice using CoinDesk API (https://api.coindesk.com/v1/bpi/currentprice.json)

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    file = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = file["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()

print(f"${number * rate:,.4f}")
