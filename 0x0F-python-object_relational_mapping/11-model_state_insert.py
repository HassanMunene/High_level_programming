#!/usr/bin/python3
"""
this module inserts a new State called Lousiana
to the table states in db hbtn_0e_6_usa
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

    state1 = State(name="Lousiana")
    session.add(state1)
    session.commit()
    print(state1.id)
