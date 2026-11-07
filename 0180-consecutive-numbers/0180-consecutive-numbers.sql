SELECT
    DISTINCT num AS ConsecutiveNums
FROM
(
SELECT
    id,
    num,
    LAG(num,1) OVER(ORDER BY id) AS prev_num1,
    LAG(num,2) OVER(ORDER BY id) AS prev_num2
FROM Logs) AS L
WHERE num = prev_num1 AND num = prev_num2;