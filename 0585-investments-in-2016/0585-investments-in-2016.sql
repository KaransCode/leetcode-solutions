SELECT 
    ROUND( SUM(tiv_2016),2) AS tiv_2016
    FROM
    (
        SELECT 
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015)  AS same_investment,
        COUNT(*) OVER (PARTITION BY lat,lon)  AS same_loc
        FROM Insurance
    ) T
    WHERE same_investment > 1 AND same_loc = 1