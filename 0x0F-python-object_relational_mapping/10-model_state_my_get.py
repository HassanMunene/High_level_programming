#!/usr/bin/python3
"""
This module recives an argument in the cli and then
filters the table in the hbtn_0e_6_usa db using the arg
as a name and the prints the id of the object retrieve if foun
or "Not found" if it does not match
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
    sysname = sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == sysname).first()

    if result:
        print(result.id)
    else:
        print("Not found")
