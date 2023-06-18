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
    state_name=sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
    )

    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states on cities.state_id=states.id WHERE states.name = %(state_name)s"
    cur.execute(query, {"state_name": state_name})

    result_query = cur.fetchall()
    city_names=[]
    for row in result_query:
        city_names.append(row[0])
    result_string = ", ".join(city_names)
    print(result_string)
    db.close()
