import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nickname = Column(String(200), unique=True)
    name = Column(String(200), nullable=False)
    surname = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    favorites = relationship("favorites")

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    characters_id = Column(Integer)
    planets_id = Column(Integer)
    vehicles_id = Column(Integer)
    user = relationship("user")  
    characters = relationship("characters")
    vehicles = relationship("vehicles")
    planets = relationship("planets")

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    gender = Column(String(6))
    hairColor = Column(String(150))
    eyeColor = Column(String(150))
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("favorites")

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    population = Column(Integer)
    diameter = Column(Integer)
    climate = Column(Integer)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("favorites")

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    model = Column(String(200))
    manufacturer = Column(String(200))
    crew = Column(String(3))
    passengers = Column(String(200))
    favorites_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("favorites")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


