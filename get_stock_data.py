import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd

load_dotenv()

api_key = os.getenv("API_KEY")

# Stock symnbols to search for in XETRA
stock_list = ["AMD.DEX", "AIR.DEX", "SIE.DEX"]

df_values = []

for stock in stock_list:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if "Global Quote" in data:
        quote = data["Global Quote"]

        # for key, value in quote.items():
        #     print(f"{key}: {value}")

        df_values.append(quote)

    else:
        print(json.dumps(data, indent=4))
