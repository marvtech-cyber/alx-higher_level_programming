#!/usr/bin/python3
"""
Lists all cities from hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    """User input for logging to Mysql."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))

    states = cur.fetchall()

    print(", ".join([state[1] for state in states]))
