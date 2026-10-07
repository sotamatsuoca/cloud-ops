SELECT ROUND(COUNT(b.player_id) / COUNT(f.player_id), 2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity b
ON b.player_id = f.player_id
AND b.event_date = f.first_login + 1;