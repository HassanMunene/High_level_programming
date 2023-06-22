#!/usr/bin/python3
"""
This module will add a new object to the State table
in essence we will add a new row called 'Lousiana'
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Lousiana")
    session.add(state)
    session.commit()

    results = session.query(State).order_by(State.id).all()

    for result in results:
        print("{}: {}".format(result.id, result.name))

    session.close()
