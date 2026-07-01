from src.config import PROJECT_ID, DATASET_ID

def get_dataset_overview():
    return f"""
    SELECT
        COUNT(*) AS total_events,
        COUNT(DISTINCT user_pseudo_id) AS total_users,
        COUNT(DISTINCT ga_session_id) AS total_sessions,
        MIN(event_date) AS start_date,
        MAX(event_date) AS end_date
    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    """

def get_event_distribution():
    return f"""
    SELECT
        event_name,
        COUNT(*) AS event_count
    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    GROUP BY event_name
    ORDER BY event_count DESC
    """

def get_device_distribution():
    return f"""
    SELECT
        device_category,
        COUNT(*) AS events
    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    GROUP BY device_category
    ORDER BY events DESC
    """

def get_source_distribution():
    return f"""
    SELECT
        session_source,
        COUNT(*) AS sessions
    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    GROUP BY session_source
    ORDER BY sessions DESC
    """

def get_country_distribution():
    return f"""
    SELECT
        country,
        COUNT(*) AS sessions
    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    GROUP BY country
    ORDER BY sessions DESC
    """

def get_session_summary():
    return f"""
    SELECT
        COUNT(*) AS total_sessions,
        AVG(session_duration_sec) AS avg_session_duration,
        AVG(total_events) AS avg_events,
        AVG(pageviews) AS avg_pageviews,
        AVG(item_views) AS avg_item_views
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    """

def get_purchase_distribution():
    return f"""
    SELECT
        purchased,
        COUNT(*) AS sessions
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    GROUP BY purchased
    ORDER BY purchased
    """

def get_checkout_abandonment_distribution():
    return f"""
    SELECT
        checkout_abandoned,
        COUNT(*) AS sessions
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    GROUP BY checkout_abandoned
    ORDER BY checkout_abandoned
    """

def get_session_duration():
    return f"""
    SELECT
        session_duration_sec
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    """

def get_total_events():
    return f"""
    SELECT
        total_events
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    """

def get_pageviews():
    return f"""
    SELECT
        pageviews
    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    """

def get_missing_summary():
    return f"""
    SELECT
        COUNT(*) AS total_rows,

        COUNTIF(user_pseudo_id IS NULL) AS missing_user,

        COUNTIF(ga_session_id IS NULL) AS missing_session,

        COUNTIF(event_name IS NULL) AS missing_event

    FROM `{PROJECT_ID}.{DATASET_ID}.stg_events`
    """

def get_duplicate_summary():
    return f"""
    SELECT

        COUNT(*) AS total_rows,

        COUNT(DISTINCT ga_session_id) AS unique_sessions

    FROM `{PROJECT_ID}.{DATASET_ID}.int_sessions`
    """


def get_funnel_data():
    return f"""
    SELECT
        *
    FROM `{PROJECT_ID}.{DATASET_ID}.mart_funnel`
    ORDER BY sessions DESC
    """

def get_checkout_abandonment_data():
    return f"""
    SELECT
        *
    FROM `{PROJECT_ID}.{DATASET_ID}.mart_checkout_abandonment`
    """

def get_purchase_prediction_data():
    return f"""
    SELECT
        *
    FROM `{PROJECT_ID}.{DATASET_ID}.mart_purchase_prediction`
    """