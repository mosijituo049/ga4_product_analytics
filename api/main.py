from fastapi import FastAPI
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.database import query_to_dataframe
import src.queries as queries

app = FastAPI(
    title="GA4 Product Analytics API",
    description="REST API for GA4 Product Analytics Project",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "GA4 Product Analytics",
        "status": "Running"
    }


@app.get("/funnel")
def get_funnel():
    df = query_to_dataframe(
        queries.get_funnel_data()
    )

    return df.to_dict(orient="records")

@app.get("/checkout")
def get_checkout():
    df = query_to_dataframe(
        queries.get_checkout_kpis()
    )

    return df.to_dict(orient="records")

@app.get(
    "/prediction",
    summary="Purchase prediction samples",
    description="Returns sample records from the purchase prediction dataset."
)
def get_prediction():
    df = query_to_dataframe(
        queries.get_purchase_prediction_data()
    )

    df = df[
        [
            "country",
            "device_category",
            "engagement_per_event",
            "checkout_ratio",
            "purchased",
        ]
    ]

    return json.loads(
        df.head(20).to_json(orient="records")
    )