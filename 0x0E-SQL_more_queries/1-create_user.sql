-- this script creates user_0d_1 in the MySQL server
-- the user should have all the privilages
-- the password of the user should be set to user_0d_1_pwd
-- if the user already exists, your script should still not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';GRANT ALL PRIVILAGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
