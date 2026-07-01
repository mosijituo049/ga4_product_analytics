from src.database import query_to_dataframe
import src.queries as queries

# ============================================================
# Data Understanding
# ============================================================
def load_dataset_overview():
    """
    Load dataset overview.
    """
    return query_to_dataframe(
        queries.get_dataset_overview()
    )

def load_event_distribution():

    return query_to_dataframe(
        queries.get_event_distribution()
    )

def load_device_distribution():

    return query_to_dataframe(
        queries.get_device_distribution()
    )

def load_source_distribution():
    """Load traffic source distribution."""
    return query_to_dataframe(
        queries.get_source_distribution()
    )

def load_country_distribution():
    """Load country distribution."""
    return query_to_dataframe(
        queries.get_country_distribution()
    )

def load_session_summary():

    return query_to_dataframe(
        queries.get_session_summary()
    )

def load_purchase_distribution():
    """Load purchase distribution."""
    return query_to_dataframe(
        queries.get_purchase_distribution()
    )


def load_checkout_distribution():
    """Load checkout abandonment distribution."""
    return query_to_dataframe(
        queries.get_checkout_abandonment_distribution()
    )


def load_session_duration():
    """Load session duration."""
    return query_to_dataframe(
        queries.get_session_duration()
    )


def load_total_events():
    """Load total events per session."""
    return query_to_dataframe(
        queries.get_total_events()
    )


def load_pageviews():
    """Load pageviews per session."""
    return query_to_dataframe(
        queries.get_pageviews()
    )

def load_missing_summary():
    """Load missing value summary."""
    return query_to_dataframe(
        queries.get_missing_summary()
    )

def load_duplicate_summary():
    """Load duplicate session summary."""
    return query_to_dataframe(
        queries.get_duplicate_summary()
    )

def load_funnel():
    return query_to_dataframe(
        queries.get_funnel_data()
    )

def load_checkout_abandonment():
    return query_to_dataframe(
        queries.get_checkout_abandonment_data()
    )

def load_purchase_prediction():
    return query_to_dataframe(
        queries.get_purchase_prediction_data()
    )