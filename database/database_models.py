from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

BASE = declarative_base()

class Persons(BASE):

    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    p_name = Column(String(250), nullable=False)
    p_type = Column(String(250), nullable=False)

class Rooms(BASE):
    ''' Creating Rooms table '''

    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    r_name = Column(String(250), nullable=False)
    r_type = Column(String(250), nullable=False)
    r_capacity = Column(Integer, nullable=False)
    r_occupued = Column(Integer, nullable=True)


class Allocations(BASE):

    __tablename__ = 'allocations'

    id = Column(Integer, primary_key=True)
    p_name = Column(String(80), nullable=False)
    o_name = Column(String(20), nullable=True)
    ls_name = Column(String(250), nullable=True)


ENGINE = create_engine('sqlite:///amity.db')
BASE.metadata.create_all(ENGINE)
