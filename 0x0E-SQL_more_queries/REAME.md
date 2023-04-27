## MySQL Constraints

constraints are placed on colums or tables. they limit the data that can be inserted into tables.
the following are constraints
1. NOT NULL
1. UNIQUE
1. PRIMARY KEY
1. FOREIGN KEY
1. ENUM
1. SET

## NOT NULL
a column with not null constraint cannot have NULL values.
```
mysql> CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
    ->                     FirstName TEXT NOT NULL, City VARCHAR(55));
Query OK, 0 rows affected (0.07 sec)
```
creates two columns with NOT NULL constraints

## UNIQUE
this ensures that all the data are unique in a column
```
mysql> CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE);
Query OK, 0 rows affected (0.08 sec)
```
here the brandname is set to be unique meaning there cannot be two brands with the same value

## PRIMARY KEY
This constraints automatically has UNIQUE constraint.
it is used to uniquely identify each record in a database table. 
it cannot be NULL, but UNIQUE KEYS can.
they become foreign key in other tables

## FOREIGN KEY
A foreign key in one table is a primary key in another table 
lets say we have two tables Authors and Books

```
mysql> CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70))
```

```
mysql> CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title VARCHAR(50),
    -> AuthorId INTEGER, FOREIGN KEY(AuthorId) REFERENCES Authors(AuthorId))
```
we create a book table, in this table we have an author id column which act as a foregin key. it references the primary key of the Authors table
we cannot insert a record into the books table with an Author id which is not present in the Authors book.

## ENUM
this is a string object with a value chosen from a list of permitted values. they are enumerated expicitly in the column specification at the creation time.

```
mysql> CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55), 
    -> Quality ENUM('High', 'Average', 'Low'));
```
we have a shops table, this table has an id, name and quality columns. the quality column is enum. it can only have three specified values : high, average and low

## SET
It can have 0 or more values and each value must be chosen from a list of permitted values.

```
mysql> CREATE TABLE Students(Id INTEGER, Name VARCHAR(55), 
    -> Certificates SET('A1', 'A2', 'B1', 'C1')); 
```
in the students table we have a certificate column each student can have zero orm more of these certificates.
this is different from enum because in ENUM you can only have one disntinct value fron the list if the permiited values

```
mysql> INSERT INTO Students VALUES(1, 'Paul', 'A1,B1');
mysql> INSERT INTO Students VALUES(2, 'Jane', 'A1,B1,A2');
mysql> INSERT INTO Students VALUES(3, 'Mark', 'A1,A2,D1,D2');
mysql> SELECT * FROM Students;
+------+------+--------------+
| Id   | Name | Certificates |
+------+------+--------------+
|    1 | Paul | A1,B1        |
|    2 | Jane | A1,A2,B1     |
|    3 | Mark | A1,A2        |
+------+------+--------------+
```

## JOIN
Sometimes we want to see data from two or more tables. to do this we need to join the tables in a way that matches up right information from each other

### NATURAL JOIN
specifies that all attributes whose values will be matched between the two tables are those with matching names.
joins two tables based on a common column, and selects records that have matching values in these columns

```
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer;
```
here the sql command selects customer_id and first_name columns from the customers table and the amount column from the orders table

the result set will contain those rows where there is a match between customer_id of the customers table and customer of the order table As shown below

![join-customer-order-table](https://github.com/HassanMunene/alx-higher_level_programming/blob/main/0x0E-SQL_more_queries/join-in-sql.png)

