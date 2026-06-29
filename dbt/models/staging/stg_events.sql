{{ config(
    materialized='view'
) }}

WITH source AS (

    SELECT *
    FROM {{ source('ga4', 'events') }}

),

renamed AS (

    SELECT

        ------------------------------------------------------------------
        -- Event Information
        ------------------------------------------------------------------

        PARSE_DATE('%Y%m%d', event_date) AS event_date,

        TIMESTAMP_MICROS(event_timestamp) AS event_timestamp,

        event_name,

        ------------------------------------------------------------------
        -- User
        ------------------------------------------------------------------

        user_pseudo_id,

        TIMESTAMP_MICROS(user_first_touch_timestamp)
            AS user_first_touch_timestamp,

        platform,

        ------------------------------------------------------------------
        -- Session (event_params)
        ------------------------------------------------------------------

        (
            SELECT value.int_value
            FROM UNNEST(event_params)
            WHERE key = 'ga_session_id'
        ) AS ga_session_id,

        (
            SELECT value.int_value
            FROM UNNEST(event_params)
            WHERE key = 'ga_session_number'
        ) AS ga_session_number,

        ------------------------------------------------------------------
        -- Page
        ------------------------------------------------------------------

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'page_location'
        ) AS page_location,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'page_title'
        ) AS page_title,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'page_referrer'
        ) AS page_referrer,

        (
            SELECT value.int_value
            FROM UNNEST(event_params)
            WHERE key = 'entrances'
        ) AS entrances,

        ------------------------------------------------------------------
        -- Engagement
        ------------------------------------------------------------------

        (
            SELECT value.int_value
            FROM UNNEST(event_params)
            WHERE key = 'engagement_time_msec'
        ) AS engagement_time_msec,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'session_engaged'
        ) AS session_engaged,

        ------------------------------------------------------------------
        -- Traffic
        ------------------------------------------------------------------

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'source'
        ) AS session_source,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'medium'
        ) AS session_medium,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'campaign'
        ) AS session_campaign,

        ------------------------------------------------------------------
        -- Device
        ------------------------------------------------------------------

        device.category AS device_category,

        device.operating_system AS operating_system,

        ------------------------------------------------------------------
        -- Geography
        ------------------------------------------------------------------

        geo.country AS country,

        ------------------------------------------------------------------
        -- Purchase
        ------------------------------------------------------------------

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'transaction_id'
        ) AS transaction_id,

        (
            SELECT COALESCE(
                value.double_value,
                CAST(value.float_value AS FLOAT64),
                CAST(value.int_value AS FLOAT64)
            )
            FROM UNNEST(event_params)
            WHERE key = 'value'
        ) AS purchase_value,

        (
            SELECT value.string_value
            FROM UNNEST(event_params)
            WHERE key = 'currency'
        ) AS currency

    FROM source

)

SELECT *
FROM renamed