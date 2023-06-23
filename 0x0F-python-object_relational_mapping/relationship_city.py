#!/usr/bin/python3
"""
This module represents the cities table
"""
from relationship_state import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer

class City(Base):
    """
    The class representation of cities
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
