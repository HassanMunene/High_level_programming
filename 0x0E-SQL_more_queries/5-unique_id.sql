-- script creates table unique_id
-- the id should be unique
-- id INT DEFAULT 1 UNIQUE, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
