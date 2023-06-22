#!/usr/bin/python3
"""
This module will be used to update the table
states where the id is 2 from its current name
to New Mexico
"""


import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

     Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).filter_by(id=2).first()
    state_obj.name = 'New Mexico'

    session.commit()
