#!/usr/bin/python3
"""
Defines a State class mapped to the 'states' table in MySQL
using SQLAlchemy ORM (Object Relational Mapping).
"""


# Import the required SQLAlchemy components
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# This creates the Base class — the foundation of all ORM models.
# Every model (table mapping) will inherit from this Base class.
Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table in the database.
    Each object of this class corresponds to one row (record) in the table.
    """

    # Name of the table that this class maps to
    __tablename__ = 'states'

    # Column definitions:
    # 'id' is an integer column, automatically generated,
    # it acts as the primary key and cannot be null.
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # 'name' is a string column (VARCHAR(128)),
    # it has a maximum length of 128 characters and cannot be null.
    name = Column(String(128), nullable=False)
