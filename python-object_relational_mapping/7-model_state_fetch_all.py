#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
Results are sorted in ascending order by states.id.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # 1. Get arguments (username, password, database name)
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Establish connection to MySQL using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # 3. Create a session (communication bridge with the DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # 5. Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # 6. Close session when done
    session.close()
