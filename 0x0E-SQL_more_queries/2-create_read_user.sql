-- the script creates a database hbtn_0d_2
-- the script also creates user_0d_2
-- the user should only have the SELECT privilage in the database hbtn_0d_2
-- the user password should be set to user_0d_2_pwd
-- if the database already exists your script should'nt fail
-- if the user alredy exists the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
