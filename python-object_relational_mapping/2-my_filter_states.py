#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Get the four command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # 2. Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # 3. Create a cursor object
    cur = conn.cursor()

    # 4. Execute a query using string formatting with format()
    # We use BINARY to make the comparison case-sensitive
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    # 5. Fetch, display and execute results
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # 6. Clean close of the cursor and connection
    cur.close()
    conn.close()
