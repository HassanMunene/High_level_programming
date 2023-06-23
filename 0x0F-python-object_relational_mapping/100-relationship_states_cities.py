#!/usr/bin/python3
"""
this scripts creates the State "Carlifornia" with the City "San Francisco"\
from the database hbtn_0e_100_usa
"""
import sys
import sqlalchemy
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]

    session.add(new_state)
    session.commit()
    session.close()
