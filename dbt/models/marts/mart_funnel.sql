{{ config(
    materialized='table'
) }}

WITH sessions AS (

    SELECT *
    FROM {{ ref('int_sessions') }}

),

funnel AS (

    ------------------------------------------------------------------
    -- Stage Counts
    ------------------------------------------------------------------

    SELECT
        1 AS stage_order,
        'Page View' AS stage,
        COUNT(*) AS sessions
    FROM sessions

    UNION ALL

    SELECT
        2,
        'View Item',
        COUNTIF(viewed_item)
    FROM sessions

    UNION ALL

    SELECT
        3,
        'Add to Cart',
        COUNTIF(cart_created)
    FROM sessions

    UNION ALL

    SELECT
        4,
        'Begin Checkout',
        COUNTIF(checkout_started)
    FROM sessions

    UNION ALL

    SELECT
        5,
        'Purchase',
        COUNTIF(purchased)
    FROM sessions

),

rates AS (

    SELECT

        stage_order,

        stage,

        sessions,

        FIRST_VALUE(sessions) OVER (
            ORDER BY stage_order
        ) AS total_sessions,

        LAG(sessions) OVER (
            ORDER BY stage_order
        ) AS previous_stage_sessions

    FROM funnel

)

SELECT

    stage,

    sessions,

    ROUND(
        sessions / total_sessions * 100,
        2
    ) AS overall_conversion_rate,

    CASE
        WHEN previous_stage_sessions IS NULL THEN 100
        ELSE ROUND(
            sessions / previous_stage_sessions * 100,
            2
        )
    END AS stage_conversion_rate,

    CASE
        WHEN previous_stage_sessions IS NULL THEN 0
        ELSE ROUND(
            100 - (sessions / previous_stage_sessions * 100),
            2
        )
    END AS stage_dropoff_rate

FROM rates

ORDER BY stage_order