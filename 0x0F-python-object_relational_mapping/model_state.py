"""
using sqlalchemy to create a table
using class and then connecting to the mysql
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}')

if __name__ == "__main__":
    from model_state import State

    Base.metadata.create_all(engine)
