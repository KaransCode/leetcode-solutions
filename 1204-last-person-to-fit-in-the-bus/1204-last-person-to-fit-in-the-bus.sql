SELECT TOP 1
    person_name
FROM 
(
SELECT
    *,
    ROW_NUMBER() OVER (ORDER BY turn) as Q_Order,
    SUM (weight) OVER (ORDER BY turn) as WeightSum
FROM Queue) t 
WHERE WeightSum <= 1000
ORDER BY WeightSum DESC;