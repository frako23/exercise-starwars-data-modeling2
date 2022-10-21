import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250),nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(50))
    manufacturer = Column(String(250))
    crew = Column(Integer)
    passengers = Column(Integer)

class CharacterFav(Base):
    __tablename__ = 'character_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer,ForeignKey ('user.id') )

class PlanetFav(Base):
    __tablename__ = 'planet_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer,ForeignKey ('user.id') )

class VehicleFav(Base):
    __tablename__ = 'vehicle_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user_id = Column(Integer,ForeignKey ('user.id') )

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')