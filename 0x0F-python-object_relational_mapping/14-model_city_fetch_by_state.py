#!/usr/bin/python3
"""
This script prints city objects from the database hbtn_0e_14_usa
in the form <state name>: <city id> <city name>
"""
import sys
import sqlalchemy
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, join

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
