import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
)
date = response.json()
price = date["bpi"]["USD"]["rate"]
price = price.replace(",", "")
amount = float(price) * bitcoin
print(f"${amount:,.4f}")
