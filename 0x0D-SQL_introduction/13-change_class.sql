-- This script will be used to remove those scores that are too low <= 5

DELETE FROM second_table WHERE score <= 5;
SELECT score, name FROM second_table ORDER BY score DESC;
