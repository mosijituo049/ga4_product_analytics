{{ config(
    materialized='table'
) }}

WITH sessions AS (

    SELECT *
    FROM {{ ref('int_sessions') }}

)

SELECT

    ------------------------------------------------------------------
    -- Funnel Counts
    ------------------------------------------------------------------

    COUNT(*) AS total_sessions,

    COUNTIF(viewed_item) AS view_item_sessions,

    COUNTIF(cart_created) AS add_to_cart_sessions,

    COUNTIF(checkout_started) AS checkout_sessions,

    COUNTIF(purchased) AS purchase_sessions,

    COUNTIF(checkout_abandoned) AS abandoned_sessions,

    ------------------------------------------------------------------
    -- Overall Funnel Conversion
    ------------------------------------------------------------------

    ROUND(
        COUNTIF(viewed_item)
        / COUNT(*) * 100,
        2
    ) AS view_item_rate,

    ROUND(
        COUNTIF(cart_created)
        / COUNT(*) * 100,
        2
    ) AS add_to_cart_rate,

    ROUND(
        COUNTIF(checkout_started)
        / COUNT(*) * 100,
        2
    ) AS checkout_rate,

    ROUND(
        COUNTIF(purchased)
        / COUNT(*) * 100,
        2
    ) AS purchase_rate,

    ------------------------------------------------------------------
    -- Stage-to-Stage Conversion
    ------------------------------------------------------------------

    ROUND(
        COUNTIF(cart_created)
        / NULLIF(COUNTIF(viewed_item),0)
        *100,
        2
    ) AS view_to_cart_rate,

    ROUND(
        COUNTIF(checkout_started)
        / NULLIF(COUNTIF(cart_created),0)
        *100,
        2
    ) AS cart_to_checkout_rate,

    ROUND(
        COUNTIF(purchased)
        / NULLIF(COUNTIF(checkout_started),0)
        *100,
        2
    ) AS checkout_to_purchase_rate,

    ------------------------------------------------------------------
    -- Checkout Abandonment
    ------------------------------------------------------------------

    ROUND(
        COUNTIF(checkout_abandoned)
        / NULLIF(COUNTIF(checkout_started),0)
        *100,
        2
    ) AS checkout_abandonment_rate

FROM sessions