#!/usr/bin/python3
"""
Lists all State objects containing the letter a
from the database hbtn_0e_6_usa, ordered by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Get arguments from the command line
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Connect to MySQL using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # 3. Create a session object for ORM queries
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query: filter with LIKE for the letter 'a', order by id
    states = (
        session.query(State)
        # use ilike('%a%') for case-insensitive
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # 5. Display results in the requested format
    for state in states:
        print(f"{state.id}: {state.name}")

    # 6. Close session properly
    session.close()
