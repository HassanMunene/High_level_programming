#!/usr/bin/python3

import sys
import sqlalchemy
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

user = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]

engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

cities = session.query(City).order_by(City.id).all()

for city in cities:
    print("{} -> {}".format(city.name, city.state.name))

session.close()
