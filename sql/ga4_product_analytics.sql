CREATE DATABASE ga4_product_analytics;

USE ga4_product_analytics;

CREATE TABLE users (
    user_id VARCHAR(100) PRIMARY KEY
);

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_category VARCHAR(50),
    operating_system VARCHAR(50)
);

CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100)
);

CREATE TABLE sessions (
    session_id BIGINT PRIMARY KEY,
    user_id VARCHAR(100),
    device_id INT,
    country_id INT,

    session_duration_sec INT,
    total_events INT,
    pageviews INT,
    item_views INT,
    searches INT,
    add_to_cart INT,
    begin_checkout INT,
    add_shipping_info INT,
    add_payment_info INT,
    purchased BOOLEAN,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (device_id) REFERENCES devices(device_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

SHOW TABLES;

