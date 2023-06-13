#!/usr/bin/python3
"""
Lists all states with N names from
hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    """User input for logging to Mysql."""

    user = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=dataBase,
                         port=3306)
    cur = db.cursor()

    querty = "SELECT * FROM states WHERE\
        name = %s COLLATE utf8mb4_bin ORDER BY id ASC;"

    cur.execute(querty, (state,))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
