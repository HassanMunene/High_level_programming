-- This is a script that creates a table called first_table in the current database in mysql
-- first_table description
-- id INT
-- name VARCHAR(256)
-- if the table exists then the script should not fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
