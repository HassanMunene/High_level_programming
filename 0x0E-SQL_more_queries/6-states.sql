-- create database hbtn_0d_usa
-- create also a table called states
-- id INT UNIQUE AUTOGEN NOT NULL PK, name VARCHAR(256)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
