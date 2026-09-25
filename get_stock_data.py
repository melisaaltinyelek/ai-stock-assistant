# %%

import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
from IPython.display import display
import time

# %%

load_dotenv()

api_key = os.getenv("API_KEY")

# Stock symnbols to search for in XETRA
stock_list = ["AMD.DEX", "AIR.DEX", "SIE.DEX", "ADS.DEX", "VOW.DEX", "RHM.DEX"]


def get_stock_data(stock_list):

    df_values = []

    for stock in stock_list:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        time.sleep(3)

        if "Global Quote" in data:
            quote = data["Global Quote"]

            # for key, value in quote.items():
            #     print(f"{key}: {value}")

            df_values.append(quote)

        else:
            print(json.dumps(data, indent=4))

    print(df_values)
    df = pd.DataFrame.from_dict(df_values)

    return df


df = get_stock_data(stock_list)
# display(df)

# %%


def clean_df_cols(df):

    new_df_cols = []

    for col in df.columns:
        print(col)
        new_col = col.split(" ", 1)[1]
        new_col = new_col.title()
        new_df_cols.append(new_col)

    # print(new_df_cols)

    df.columns = new_df_cols

    # print(df.columns)

    return df


df = clean_df_cols(df)
display(df)

# %%

df.to_csv("data/stock_data.csv", index=False)

# %%


def get_user_budget():

    budget = input("Enter your budget (EUR): ")

    try:
        budget = float(budget)
        return budget

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_user_budget()


user_budget = get_user_budget()


# %%

stock_df = pd.read_csv("data/stock_data.csv")
stock_df.dtypes


def display_stocks(budget):

    filtered_df = stock_df[stock_df["Price"] <= budget]
    if not filtered_df.empty:
        return filtered_df
    else:
        print(f"No stock has been found in the budget of {budget}€.")


display_stocks(budget=user_budget)

# %%
