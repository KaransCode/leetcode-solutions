-- Feb 2020 AND unit >= 100

SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM Products P
LEFT JOIN Orders o
ON p.product_id = o.product_id
WHERE Year(order_date) = 2020 AND Month(order_date) = 2
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;