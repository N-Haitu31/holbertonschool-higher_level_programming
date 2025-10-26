#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # 1. Retrieve arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]  # the state name to search for

    # 2. Connect to MySQL database using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # 3. Create a session to interact with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Filter by state name (Safe, no SQL injection)
    state = session.query(State).filter(State.name == search_name).first()

    # 5. Display result or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # 6. Close the session properly
    session.close()
