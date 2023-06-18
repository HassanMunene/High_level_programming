#!/usr/bin/python3
"""
This script joins the cities and states
table to produce a city with their repective state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
    )

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC"
    cur.execute(query)

    result_query = cur.fetchall()
    for row in result_query:
        print(row)

    db.close()
