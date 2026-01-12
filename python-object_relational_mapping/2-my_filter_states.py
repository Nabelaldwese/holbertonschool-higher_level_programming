#!/usr/bin/python3
"""
Displays all states where name matches the user input.
"""

import sys
import MySQLdb


def main():
    """Connects to MySQL and prints matching states."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(
        state_name
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
