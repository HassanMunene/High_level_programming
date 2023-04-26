# Introduction to SQL 

When we will be making applications we will require a place where we can store the data

Data will be stored in a database and the way to communicate, manipulate, and retrieve this data we require a language
that will be able to communicate with the database, just like how we need a programming language to give a computer instructions we also a specific tool that can communicate with database.

This language is called STRUCTURED QUERY LANGUAGE(SQL). 

The type of database is used to manipulate is called a relational database, as it made up of tables that are somehow connected.

## Installing MySQL
MySQL is an open-source dbms commonly installed as part of the popular LAMP(Linux, Apache, MySQL, PHP/Python/Pearl) stack. 

SQL statements are divided into two major categories:
1. data defination language
1. data manipulation language

## data defination language(DDL)
used to build and modify the structure of your tables and other objects in the database.
- create table
```
CREATE TABLE <table name>(
<attribute name><data type>,
...
<attribute name> <datatype>);
```
the data types that are used mostly are,
- character strings eg. VARCHAR, CHAR
- numeric types e.g. NUMBER, INTEG

The alter table statement may be used to specify primary and foreign key constraints, as well as to make other modifictions to the table structure
```
ALTER TABLE <table name>
ADD CONSTRAINT <constraint name> PRIMARY KEY (<attribute list>)
```
the conraint name you can use the following convention (customer_pk)
so you can remember easily. the attribute list contains the one or more attributes that form this pk

The foreign key is a bit more complicated since you have to specify both the fk attribute in this child table and the pk attributes that they link to in the parent table

```
ALTER TABLE <table name>
ADD CONSTRAINTS <constaints name> FOREIGN KEY (<attribute list>)
REFERENCES <parent table name> (<attribute list>);
```

## Data manipulation language(DML)
these statements are used to work with the data in the tables. 
1. the insert statement is used to add new rows to a table
```
INSERT INTO <table name>
VALUES (<value1>, ..., <valuen>);
```
the comma delimeter list of values must match the table structure 
the update statement is used to change the values that are already in table


