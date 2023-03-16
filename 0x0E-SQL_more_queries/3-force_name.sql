-- scripts creates a table force_name on MySQL server
-- id INT, name VARCHAR(2560 NOT NULL
-- if table already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256) NOT NULL);
