SELECT
    MAX(num) AS num
FROM
(
SELECT
    num,
    COUNT(*) OVER (PARTITION BY num) AS num_count
FROM MyNumbers) t 
WHERE num_count = 1;