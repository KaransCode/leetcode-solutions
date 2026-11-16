SELECT results
FROM(
    SELECT TOP 1 
    u.name AS results
    FROM MovieRating AS r 
    JOIN Users AS u 
    ON u.user_id = r.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    ) A

    UNION ALL
SELECT results
FROM(
    SELECT TOP 1 
    m.title AS results
    FROM MovieRating AS r
    JOIN Movies AS m
    ON m.movie_id = r.movie_id
    WHERE YEAR(r.created_at) = 2020
    AND MONTH(r.created_at) = 2
    GROUP BY m.title, m.movie_id
    ORDER BY AVG(CAST(r.rating AS DECIMAL(10,2))) DESC,
    m.title ASC) B;