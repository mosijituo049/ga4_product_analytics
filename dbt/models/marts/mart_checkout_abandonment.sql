{{ config(
    materialized='table'
) }}

WITH sessions AS (

    SELECT *
    FROM {{ ref('int_sessions') }}

)

SELECT

    ------------------------------------------------------------------
    -- Keys
    ------------------------------------------------------------------

    ga_session_id,
    user_pseudo_id,

    ------------------------------------------------------------------
    -- Target Variables
    ------------------------------------------------------------------

    purchased,

    checkout_abandoned,

    ------------------------------------------------------------------
    -- Session Metrics
    ------------------------------------------------------------------

    session_start,
    session_end,
    session_duration_sec,

    total_events,
    total_engagement_time,

    ------------------------------------------------------------------
    -- Funnel Behaviour
    ------------------------------------------------------------------

    pageviews,
    unique_pages,

    item_views,

    searches,

    add_to_cart,

    begin_checkout,

    add_shipping_info,

    add_payment_info,

    ------------------------------------------------------------------
    -- Device & Acquisition
    ------------------------------------------------------------------

    device_category,

    operating_system,

    country,

    session_source,

    session_medium,

    session_campaign

FROM sessions

WHERE checkout_started = TRUE