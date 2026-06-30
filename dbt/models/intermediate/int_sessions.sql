{{ config(
    materialized='table'
) }}

WITH events AS (

    SELECT *
    FROM {{ ref('stg_events') }}

),

session_metrics AS (

    SELECT

        ------------------------------------------------------------------
        -- Session Keys
        ------------------------------------------------------------------

        ga_session_id,

        ANY_VALUE(user_pseudo_id) AS user_pseudo_id,

        ------------------------------------------------------------------
        -- Session Time
        ------------------------------------------------------------------

        MIN(event_timestamp) AS session_start,

        MAX(event_timestamp) AS session_end,

        TIMESTAMP_DIFF(
            MAX(event_timestamp),
            MIN(event_timestamp),
            SECOND
        ) AS session_duration_sec,

        ------------------------------------------------------------------
        -- Event Counts
        ------------------------------------------------------------------
        COUNT(*) AS total_events,

        COUNT(DISTINCT page_location) AS unique_pages,

        COUNTIF(event_name = 'page_view') AS pageviews,

        COUNTIF(event_name = 'view_item') AS item_views,

        COUNTIF(event_name = 'view_search_results') AS searches,

        COUNTIF(event_name = 'add_to_cart') AS add_to_cart,

        COUNTIF(event_name = 'begin_checkout') AS begin_checkout,

        COUNTIF(event_name = 'add_shipping_info') AS add_shipping_info,

        COUNTIF(event_name = 'add_payment_info') AS add_payment_info,

        COUNTIF(event_name = 'purchase') AS purchases,

        ------------------------------------------------------------------
        -- Funnel Flags
        ------------------------------------------------------------------

        MAX(event_name = 'view_item') AS viewed_item,

        MAX(event_name = 'add_to_cart') AS cart_created,

        MAX(event_name = 'begin_checkout') AS checkout_started,

        MAX(event_name = 'purchase') AS purchased,

        ------------------------------------------------------------------
        -- Checkout Abandonment
        ------------------------------------------------------------------

        CASE

            WHEN
                MAX(event_name = 'begin_checkout')
                AND NOT MAX(event_name = 'purchase')

            THEN TRUE

            ELSE FALSE

        END AS checkout_abandoned,

        ------------------------------------------------------------------
        -- Engagement
        ------------------------------------------------------------------

        /*SUM(engagement_time_msec) AS total_engagement_time,*/

        COALESCE(
            SUM(engagement_time_msec),
            0
        ) AS total_engagement_time,

        MAX(session_engaged) AS session_engaged,

        ------------------------------------------------------------------
        -- Session Dimensions
        ------------------------------------------------------------------

        ANY_VALUE(device_category) AS device_category,

        ANY_VALUE(operating_system) AS operating_system,

        ANY_VALUE(country) AS country,

        ANY_VALUE(session_source) AS session_source,

        ANY_VALUE(session_medium) AS session_medium,

        ANY_VALUE(session_campaign) AS session_campaign

    FROM events

    GROUP BY ga_session_id

)

SELECT *
FROM session_metrics