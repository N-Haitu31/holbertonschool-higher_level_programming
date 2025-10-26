#!/usr/bin/python3
"""
Script that changes the name of the State object with id=2 to 'New Mexico'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Get CLI arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 2. Connect to MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # 3. Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Retrieve the State object with id=2
    state = session.query(State).get(2)

    # 5. Update the name if the record exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # 6. Close the session
    session.close()
