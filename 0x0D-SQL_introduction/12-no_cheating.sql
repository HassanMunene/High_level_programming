-- This script will be used to update the score of a certain record whose name is Bob

UPDATE second_table SET score = 10 WHERE name = "Bob";
SELECT score, name FROM second_table;
