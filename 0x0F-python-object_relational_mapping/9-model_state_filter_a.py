#!/usr/bin/python3
"""
This module filters the table and returns
data whose name has a letter "a" in it
it then orders the data by id in ascending order
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

    results = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id)

    for query in results:
        print('{}: {}'.format(query.id, query.name))
