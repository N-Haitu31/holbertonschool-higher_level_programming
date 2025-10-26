#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # 1. Get command-line arguments
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

    # 3. Create a cursor to execute SQL queries
    cur = conn.cursor()

    # 4. Execute a parameterized query to avoid SQL injection
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # 5. Fetch all city names
    rows = cur.fetchall()

    # 6. Display all city names separated by ", "
    print(", ".join([row[0] for row in rows]))

    # 7. Close the cursor and connection
    cur.close()
    conn.close()
