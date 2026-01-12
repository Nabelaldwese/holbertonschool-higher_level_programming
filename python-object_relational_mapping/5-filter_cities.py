#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Cities are printed on one line separated by ", ".
"""

import sys
import MySQLdb


def main():
    """Connects to MySQL and prints cities for the given state safely."""
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

    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;",
        (state_name,)
    )

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
