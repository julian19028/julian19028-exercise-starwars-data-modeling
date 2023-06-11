import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Height = Column(Integer, nullable=False)
    Mass = Column(Integer, nullable=False)
    Hair_Color = Column (String(250), nullable=False)
    Skin_Color = Column (String(250), nullable=False)
    Birth_Year = Column (String(250), nullable=True)
    Gender = Column (String(250), nullable=False)
    Homewolrd = Column (Integer, nullable=False)
    Principal = relationship("Principal")

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    Principal = relationship("Principal")

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Last_Name = Column(String(250))
    Email = Column(String(250), nullable=False)
    Principal = relationship("Principal") 

class Principal(Base):
    __tablename__ = 'Principal'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('Users.id'))
    users = relationship("Users", back_populates="Principal")
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    planets = relationship("Planets", back_populates="Principal")
    People_id = Column(Integer, ForeignKey('People.id'))
    People = relationship("People")   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
