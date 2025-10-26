#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the MySQL username, password, and database name
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 1. Connect to the MySQL database using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True  # Check if the connection is alive before every use
    )

    # 2. Create a Session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Query all State objects whose name contains the letter 'a'
    # This is equivalent to SQL: SELECT * FROM states WHERE name LIKE '%a%';
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # 4. For each State found, mark it for deletion from the session
    for state in states_with_a:
        # The object is scheduled to be removed from the database
        session.delete(state)

    # 5. Commit the transaction to apply (save) all deletions to the database
    # All states marked for deletion are now removed in the database
    session.commit()

    # 6. Close the session to free resources
    session.close()
