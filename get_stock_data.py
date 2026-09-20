import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("API_KEY")

# Stock symnbols to search for
stock_list = ["AMD.DEX", "AIR.DEX", "SIE.DEX"]

for stock in stock_list:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))
