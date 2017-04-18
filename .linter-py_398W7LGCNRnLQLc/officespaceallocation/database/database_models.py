from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BASE = declarative_base()

class Persons(BASE):

    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    person_name = Column(String(250), nullable=False)
    person_type = Column(String(250), nullable=False)

class Rooms(BASE):
    ''' Creating Rooms table '''

    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)
    room_capacity = Column(Integer, nullable=False)

class Allocations(BASE):

    __tablename__ = 'allocations'

    id = Column(Integer, primary_key=True)
    person_name = Column(String(80), nullable=False)
    office_name = Column(String(20), nullable=True)
    livingspace_name = Column(String(250), nullable=True)


ENGINE = create_engine('sqlite:///amity.db')
BASE.metadata.create_all(ENGINE)
