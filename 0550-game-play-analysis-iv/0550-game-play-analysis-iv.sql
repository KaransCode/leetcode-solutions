SELECT
    ROUND( COUNT(DISTINCT A.player_id) * 1.00/ 
    COUNT ( DISTINCT B.player_id),2) AS fraction
FROM
    (SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity 
    GROUP BY player_id ) B
    LEFT JOIN Activity A
    ON A.player_id = B.player_id 
    AND DATEDIFF(day, B.first_login, A.event_date) = 1 ;