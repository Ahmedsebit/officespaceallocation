from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BASE = declarative_base()

class Persons(BASE):
    '''
    Class for creating the person table in the database
    '''

    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    person_name = Column(String(250), nullable=False)
    person_type = Column(String(250), nullable=False)
    office_name = Column(String(20), nullable=True)
    livingspace_name = Column(String(250), nullable=True)

class Rooms(BASE):
    '''
    Class for creating the room table in the database
    '''

    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    room_name = Column(String(250), nullable=False)
    room_type = Column(String(250), nullable=False)


class Initialize(object):
    '''
    The function initaializes the database through a new databse or an existing database.
    '''

    def initialize(filename):
        ENGINE = create_engine('sqlite:///'+filename)
        BASE.metadata.create_all(ENGINE)
