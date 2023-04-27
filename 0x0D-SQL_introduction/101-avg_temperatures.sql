-- this script uses the temperature table in the hbtn_oc_0 database
-- to find the average temp of each city creates a field avg_temp
-- and displays the average temp by city ordered by temp

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

