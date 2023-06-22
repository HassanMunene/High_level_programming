#!/usr/bin/python3
"""
using sqlalchemy to create a table
using class and then connecting to the mysql
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    this is the class that represents
    the table states, the attributes rep
    the columns of the table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
