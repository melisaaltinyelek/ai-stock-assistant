# %%
import yfinance as yf
from yfinance import EquityQuery
import json
import pandas as pd
from IPython.display import display

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


def get_stock_data(user_budger):

    df_values = []

    q = EquityQuery(
        "and",
        [
            EquityQuery("EQ", ["exchange", "GER"]),
            EquityQuery("LTE", ["intradayprice", user_budget]),
        ],
    )

    response = yf.screen(q, sortField="ticker", sortAsc=True)

    print(json.dumps(response, indent=4))

    if "quotes" in response:
        quote = response["quotes"]

        print(quote)

        for val in quote:
            # print(val)
            # for key, value in val.items():
            #     print(f"Key: {key}, Value: {value}")

            df_values.extend(quote)
    else:
        print(json.dumps(response, indent=4))

    print(df_values)
    df = pd.DataFrame.from_dict(df_values)
    return df


df = get_stock_data(user_budger=user_budget)
# display(df)
# %%

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

display(df)

# &&


def clean_df_cols(df):

    new_df_cols = []

    for col in df.columns:
        print(col)
        new_col = col.title()
        new_df_cols.append(new_col)

    # print(new_df_cols)

    df.columns = new_df_cols

    # print(df.columns)

    return df


df = clean_df_cols(df)
display(df)
# %%

df.to_csv("data/yfinance_stock_data.csv")
# %%
