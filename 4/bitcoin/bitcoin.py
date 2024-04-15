import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    jsonfile = response.json()
except requests.RequestException:
    pass

rate = float(jsonfile["bpi"]["USD"]['rate'].replace(",", ""))
amount = rate * n
print(f"${amount:,.4f}")
