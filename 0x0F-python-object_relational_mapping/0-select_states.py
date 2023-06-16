#!/usr/bin/python3
"""
We will use MySQLdb module to connect to our database
and the create a cursor that we will use to execute our queries
and then carry out our query to select all the states from the table states
then order them in ascending order by id
from there we will fetch the result of the query and print each on its ows line
finally we will close the connection
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,password=password, db=database, port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_results = cur.fetchall()
    for row in query_results:
        print(row)
    db.close()
