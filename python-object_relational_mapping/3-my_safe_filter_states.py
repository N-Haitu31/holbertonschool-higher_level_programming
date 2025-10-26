#!/usr/bin/python3
"""
Lists all states with a given name from the database
safely against SQL injection..
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Extract arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # 2. Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # 3. Create cursor
    cur = conn.cursor()

    # 4. Use parameterized query (Protected against SQL Injection)
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (state_name,)
    )

    # 5. Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # 6. Close everything cleanly
    cur.close()
    conn.close()
