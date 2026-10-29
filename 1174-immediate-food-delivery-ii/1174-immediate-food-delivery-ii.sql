SELECT
    ROUND(AVG(  CASE 
                    WHEN order_date = customer_pref_delivery_date THEN 100.0
                    ELSE 0.0
                END
          ),2) AS immediate_percentage
FROM
    (   SELECT
            *,
            ROW_NUMBER () OVER(PARTITION BY customer_id ORDER BY order_date ASC) AS 
            Order_Rank
        FROM Delivery )T
WHERE Order_Rank = 1