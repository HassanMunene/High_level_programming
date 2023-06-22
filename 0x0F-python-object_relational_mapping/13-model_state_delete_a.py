#!/usr/bin/python3
"""
This modlue id used to delete rows from the table states\
which contain letter 'a' in their name
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

    results = session.query(State).filter(State.name.like("%a%")).all()

    for result in results:
        session.delete(result)

    session.commit()
