#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Retrieve command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Connect to MySQL with UTF-8 support
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # 3. Create a cursor to execute queries
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # 4. Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # 5. Clean closure of resources
    cur.close()
    conn.close()
