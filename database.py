# %%

from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Uuid
import os
import psycopg

# %%

load_dotenv()
database_url = os.getenv("DB_URL")

# %%

engine = create_engine(database_url)

# %%

# with engine.connect() as connection:
#     rows = connection.execute(text("SELECT * FROM search_requests")).fetchall()

# print(rows)

# %%

sql = text("""
    INSERT INTO search_requests (request_id, budget_eur)
    VALUES (:request_id, :budget);
""")

# %%


def save_search_request(request_id, budget, df):

    input_dict = {"request_id": request_id, "budget": budget}
    with engine.begin() as connection:
        connection.execute(sql, input_dict)
        df.to_sql(
            name="search_results",
            con=connection,
            if_exists="append",
            index=False,
            dtype={"request_id": Uuid},
        )
