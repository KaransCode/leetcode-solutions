SELECT 
    DISTINCT
    name
FROM SalesPerson
WHERE sales_id NOT IN
    (
    SELECT 
        O.sales_id
    FROM Orders AS O
    LEFT JOIN Company AS C
    ON C.com_id = O.com_id
    WHERE C.name = 'RED')