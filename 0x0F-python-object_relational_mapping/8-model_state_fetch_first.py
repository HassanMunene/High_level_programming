#!/usr/bin/python3
"""
This module queries the states table
in hbtn_0e_6 db and returns the first row
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
