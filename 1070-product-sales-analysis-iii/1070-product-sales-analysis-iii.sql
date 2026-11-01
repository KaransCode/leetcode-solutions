SELECT product_id, year AS first_year, quantity, price
FROM 
(
SELECT
    *,
    RANK() OVER (PARTITION BY product_id ORDER BY year ASC) AS year_rank
FROM Sales) t
WHERE year_rank = 1;