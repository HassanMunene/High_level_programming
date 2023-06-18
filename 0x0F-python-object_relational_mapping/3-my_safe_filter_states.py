#!/usr/bin/python3
"""
This script is implemented so at to avoid
sql injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
    )

    cur = db.cursor()
    query =  "SELECT * FROM states WHERE name = %(state_name)s ORDER BY id ASC"
    cur.execute(query, {'state_name':state_name})

    result_query = cur.fetchall()
    for row in result_query:
        print(row)

    db.close()
