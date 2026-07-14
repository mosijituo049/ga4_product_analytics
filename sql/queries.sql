-- Top Countries
SELECT
    c.country_name,
    COUNT(*) AS sessions
FROM sessions s
JOIN countries c
ON s.country_id = c.country_id
GROUP BY c.country_name
ORDER BY sessions DESC
LIMIT 10;

-- Device Distribution
SELECT
    d.device_category,
    COUNT(*) AS sessions
FROM sessions s
JOIN devices d
ON s.device_id = d.device_id
GROUP BY d.device_category;

-- Purchase Rate
SELECT
    purchased,
    COUNT(*) AS sessions
FROM sessions
GROUP BY purchased;

-- Checkout Conversion
SELECT
    SUM(begin_checkout > 0) AS checkout_sessions,
    SUM(purchased = 1) AS purchase_sessions,
    ROUND(
        SUM(purchased = 1) / SUM(begin_checkout > 0) * 100,
        2
    ) AS checkout_conversion_rate
FROM sessions;

-- Device Purchase Performance
SELECT
    d.device_category,
    ROUND(AVG(pageviews), 2) AS avg_pageviews,
    ROUND(AVG(session_duration_sec), 2) AS avg_duration
FROM sessions s
JOIN devices d
ON s.device_id = d.device_id
GROUP BY d.device_category;

