#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Amenities class representation"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # relationship between Amenity Place and Amenity
