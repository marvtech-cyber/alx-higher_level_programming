#!/usr/bin/python3
"""
Prints the first State object.
"""
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    ENGINE = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    SQLSes = sessionmaker(bind=ENGINE)
    session = SQLSes()
    STCity = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in STCity:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
