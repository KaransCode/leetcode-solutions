SELECT 
    M.name
    FROM Employee M
    JOIN Employee E
    ON M.id = E.managerId
GROUP BY M.id, M.name
HAVING COUNT(*) >= 5;