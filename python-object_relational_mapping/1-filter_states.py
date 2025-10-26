#!/usr/bin/python3
"""
Script that lists all states with names starting with 'N'
from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Get command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Establish connection to the MySQL server localhost, port 3306
    # charset="utf8" handling of special characters (accents, etc.)
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8",
    )

    # 3. Create a cursor object to send SQL queries and get results back
    cur = conn.cursor()

    # 4. Execute a SQL query:
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC;"
    )

    # 5. Fetch all results returned by the query (as a list of tuples)
    rows = cur.fetchall()
    # Print each row. Each row is a tuple: (id, name)
    for row in rows:
        print(row)

    # 6. Close the cursor (to free memory) and then the database connection
    cur.close()
    conn.close()
