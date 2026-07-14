from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine, text
from src.config import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DATABASE,
    MYSQL_USER,
    MYSQL_PASSWORD,
)

from src.database import query_to_dataframe
import src.queries as queries

# -------------------------------------------------------
# MySQL Connection
# -------------------------------------------------------

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

# -------------------------------------------------------
# Load data from BigQuery
# -------------------------------------------------------

df = query_to_dataframe(
    queries.get_sessions()
)

df = df.head(10000)

print(f"Loaded {len(df)} sessions from BigQuery.")

# -------------------------------------------------------
# Clear existing data
# -------------------------------------------------------

with engine.begin() as conn:
    conn.execute(text("DELETE FROM sessions"))
    conn.execute(text("DELETE FROM devices"))
    conn.execute(text("DELETE FROM countries"))
    conn.execute(text("DELETE FROM users"))

# -------------------------------------------------------
# Users
# -------------------------------------------------------

users = (
    df[["user_pseudo_id"]]
    .drop_duplicates()
    .rename(columns={"user_pseudo_id": "user_id"})
)

users.to_sql(
    "users",
    engine,
    if_exists="append",
    index=False,
)

print("Users imported.")

# -------------------------------------------------------
# Devices
# -------------------------------------------------------

devices = (
    df[["device_category", "operating_system"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

devices.index += 1
devices.insert(0, "device_id", devices.index)

devices.to_sql(
    "devices",
    engine,
    if_exists="append",
    index=False,
)

print("Devices imported.")

# -------------------------------------------------------
# Countries
# -------------------------------------------------------

countries = (
    df[["country"]]
    .drop_duplicates()
    .rename(columns={"country": "country_name"})
    .reset_index(drop=True)
)

countries.index += 1
countries.insert(0, "country_id", countries.index)

countries.to_sql(
    "countries",
    engine,
    if_exists="append",
    index=False,
)

print("Countries imported.")

# -------------------------------------------------------
# Build lookup tables
# -------------------------------------------------------

device_lookup = dict(
    zip(
        devices.device_category + "_" + devices.operating_system,
        devices.device_id,
    )
)

country_lookup = dict(
    zip(
        countries.country_name,
        countries.country_id,
    )
)

# -------------------------------------------------------
# Sessions
# -------------------------------------------------------

sessions = df.copy()

sessions["device_id"] = (
    sessions["device_category"]
    + "_"
    + sessions["operating_system"]
).map(device_lookup)

sessions["country_id"] = sessions["country"].map(country_lookup)

sessions = sessions.rename(
    columns={
        "ga_session_id": "session_id",
        "user_pseudo_id": "user_id",
    }
)

sessions = sessions[
    [
        "session_id",
        "user_id",
        "device_id",
        "country_id",
        "session_duration_sec",
        "total_events",
        "pageviews",
        "item_views",
        "searches",
        "add_to_cart",
        "begin_checkout",
        "add_shipping_info",
        "add_payment_info",
        "purchased",
    ]
]

sessions["purchased"] = sessions["purchased"].astype(bool)

sessions.to_sql(
    "sessions",
    engine,
    if_exists="append",
    index=False,
)

print("Sessions imported.")

print("Done!")