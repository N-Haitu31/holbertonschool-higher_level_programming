#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
in the format: <state name>: (<city id>) <city name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # 1. Get CLI arguments
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # 2. Connect to MySQL with SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Query all cities joined with their states, ordered by city id
    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # 4. Print each city and its state as requested
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
