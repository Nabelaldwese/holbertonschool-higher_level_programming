#!/usr/bin/python3
"""
2-my_filter_states.py

Takes MySQL credentials and a state name, then displays matching rows
from the states table in hbtn_0e_0_usa sorted by id (ascending).
Uses MySQLdb and SQL query string formatting with user input.
"""

import sys
import MySQLdb


def main():
    """Entry point."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    cur = db.cursor()

    # Must use format with user input (as per task requirement)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()

