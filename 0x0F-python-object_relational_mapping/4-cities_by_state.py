#!/usr/bin/python3
"""
Lists all cities from hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    """User input for logging to Mysql."""

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=dataBase,
                         port=3306)

    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              ORDER BY cities.id ASC"
    cur.execute(query,)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
