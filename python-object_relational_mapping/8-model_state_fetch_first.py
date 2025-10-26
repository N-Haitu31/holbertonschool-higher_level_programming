#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Retrieve command-line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Establish connection to MySQL database using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # 3. Create a Session object (used to interact with the DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # 5. Display the result or "Nothing" if table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # 6. Close session
    session.close()
