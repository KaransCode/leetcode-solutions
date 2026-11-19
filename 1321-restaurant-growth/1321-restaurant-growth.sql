WITH DailySales AS
(
    SELECT 
    visited_on,
    SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on )
    SELECT 
        visited_on,
        amount,
        average_amount
        FROM
        (
            SELECT 
                visited_on,
                SUM(amount) OVER (ORDER BY visited_on ASC 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,

                ROUND(AVG(1.0 * amount) OVER (ORDER BY visited_on ASC
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ), 2) AS average_amount,

                ROW_NUMBER() OVER (ORDER BY visited_on) AS rdays
            FROM DailySales) D
            WHERE rdays >= 7
