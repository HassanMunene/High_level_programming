-- this script displays the max tempererature of each state
-- ordered by state name

SELECT State, MAX(value) AS max_temp
FROM temperatures
GROUP BY State
ORDER BY State
