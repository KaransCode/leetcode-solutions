SELECT 
    DISTINCT
    T.id AS id,
    CASE
        WHEN T.p_id IS NULL THEN 'Root'
        WHEN N.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree AS T
LEFT JOIN Tree AS N
ON T.id = N.p_id;