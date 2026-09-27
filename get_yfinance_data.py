# %%

import yfinance as yf
from yfinance import EquityQuery
import json
import pandas as pd
from IPython.display import display
import re
import uuid

# %%


def get_user_budget():

    budget = input("Enter your budget (EUR): ")

    try:
        budget = float(budget)
        return budget

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_user_budget()


# user_budget = get_user_budget()

# %%


def get_stock_data(user_budget):

    df_values = []

    q = EquityQuery(
        "and",
        [
            EquityQuery("EQ", ["exchange", "GER"]),
            EquityQuery("LTE", ["intradayprice", user_budget]),
        ],
    )

    response = yf.screen(q, size=250, sortField="ticker", sortAsc=True)

    print(json.dumps(response, indent=4))

    if "quotes" in response:
        quote = response["quotes"]

        print(quote)

        # for val in quote:
        #     # print(val)
        #     # for key, value in val.items():
        #     #     print(f"Key: {key}, Value: {value}")

        df_values.extend(quote)
    else:
        print(json.dumps(response, indent=4))

    # print(df_values)

    df = pd.DataFrame.from_dict(df_values)

    return df


# df = get_stock_data(user_budger=user_budget)
# display(df)
# %%


def clean_df_cols(df):

    new_df_cols = []

    for col in df.columns:
        # print(col)
        col = re.sub(r"([a-z])([A-Z])", r"\1 \2", col)
        # print(col)
        new_col = col.title()
        new_df_cols.append(new_col)

    # print(new_df_cols)

    df.columns = new_df_cols

    # print(df.columns)

    return df


# %%


def display_stocks(budget):

    filtered_df = stock_df[stock_df["Regular Market Price"] <= budget]
    if not filtered_df.empty:
        return filtered_df
    else:
        print(f"No stock has been found in the budget of {budget}€.")


# %%

request_id = str(uuid.uuid4())
# print(request_id)

file_name = request_id[0:8]
# print(file_name)

user_budget = get_user_budget()
df = get_stock_data(user_budget=user_budget)

df = df[
    [
        "symbol",
        "longName",
        "regularMarketPrice",
        "currency",
        "fullExchangeName",
        "regularMarketTime",
    ]
]

df = clean_df_cols(df)

df = df.assign(Request_ID=request_id)

df.rename(
    columns={
        "Symbol": "Symbol",
        "Long Name": "Company Name",
        "Regular Market Price": "Regular Market Price",
        "Currency": "Currency",
        "Full Exchange Name": "Exchange",
        "Regular Market Time": "Quote Time",
        "Request_ID": "Request ID",
    },
    inplace=True,
)

df.duplicated(subset="Symbol", keep=False).any()
df = df.dropna()

display(df)

# %%

df.to_csv(f"data/yfinance_stock_data_{file_name}.csv", index=False)

# %%

stock_df = pd.read_csv(f"data/yfinance_stock_data_{file_name}.csv")

display_stocks(user_budget)

# %%
