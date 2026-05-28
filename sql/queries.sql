-- 1. Verificar cantidad de registros cargados
SELECT COUNT(*) AS total_registros
FROM sales_data;

-- 2. Ventas totales por categoría
SELECT
    category_name,
    SUM(total_price) AS total_ventas
FROM sales_data
GROUP BY category_name
ORDER BY total_ventas DESC;

-- 3. Top 10 productos más vendidos
SELECT
    product_name,
    SUM(quantity) AS unidades_vendidas
FROM sales_data
GROUP BY product_name
ORDER BY unidades_vendidas DESC
LIMIT 10;

-- 4. Ventas por tienda
SELECT
    store_name,
    SUM(total_price) AS total_ventas
FROM sales_data
GROUP BY store_name
ORDER BY total_ventas DESC;

-- 5. Órdenes totales
SELECT
    COUNT(DISTINCT order_id) AS ordenes_totales
FROM sales_data;

-- 6. Productos vendidos
SELECT
    SUM(quantity) AS productos_vendidos
FROM sales_data;

-- 7. Ventas totales generales
SELECT
    SUM(total_price) AS ventas_totales
FROM sales_data;