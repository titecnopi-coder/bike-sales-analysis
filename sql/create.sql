CREATE TABLE sales_data (
    order_id INT,
    customer_id INT,
    order_status INT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    store_id INT,
    staff_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    item_id INT,
    product_id INT,
    product_name VARCHAR(150),
    category_name VARCHAR(100),
    quantity INT,
    list_price NUMERIC(10,2),
    discount NUMERIC(5,2),
    total_price NUMERIC(12,2)
);

SELECT COUNT(*)
FROM sales_data;

SELECT
    category_name,
    SUM(total_price) AS total_ventas
FROM sales_data
GROUP BY category_name
ORDER BY total_ventas DESC;

SELECT
    category_name,
    SUM(REPLACE(total_price, ',', '.')::numeric) AS total_ventas
FROM sales_data
GROUP BY category_name
ORDER BY total_ventas DESC;

ALTER TABLE sales_data
ALTER COLUMN total_price TYPE numeric
USING REPLACE(total_price, ',', '.')::numeric;