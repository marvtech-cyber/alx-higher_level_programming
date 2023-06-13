#!/usr/bin/python3
"""
Lists all states with N names from
hbtn_0e_0_usa database.
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        if state[1][0] == "N":
            print(state)
    cur.close()
    db.close()
