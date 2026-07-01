# src/database.py
import streamlit as st
from google.cloud import bigquery
from src.config import PROJECT_ID

@st.cache_resource
def get_client():
    """
    Return a BigQuery client.
    """
    return bigquery.Client(project=PROJECT_ID)

def query_to_dataframe(query: str):
    """
    Execute SQL and return a pandas DataFrame.
    """
    client = get_client()
    return client.query(query).to_dataframe()