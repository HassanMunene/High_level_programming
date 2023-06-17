#!/usr/bin/python3
"""
This script filters the states in the
hbtn_0e_0_usa database by matching their
name with the name provided in the argv[4]
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user = username, password=password, database=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = 'state_name' ORDER BY id ASC")

    result_query = cur.fetchall()
    for row in result_query:
        print(row)

    db.close()
