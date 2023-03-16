-- the script creates a database hbtn_0d_2 and user_0d_2
-- the user should only have SELECT privilage in the database hbtn_0d_2
-- the user password should be set to user_0d_2_pwd
-- if the database already exists your script should'nt fail and the same for user

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER OF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
