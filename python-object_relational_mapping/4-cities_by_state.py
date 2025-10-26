#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Get the command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # 3. Create a cursor to execute SQL queries
    cur = conn.cursor()

    # 4. Execute a single JOIN query
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    # 5. Fetch all rows and display them
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # 6. Close the cursor and connection
    cur.close()
    conn.close()
