from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Persons, Rooms, Allocations, BASE

ENGINE = create_engine('sqlite:///amity.db')

BASE.metadata.create_all(ENGINE)
DBSESSION = sessionmaker(bind=ENGINE)
SESSIONS = DBSESSION()

def get_persons():
    persons = SESSIONS.query(Persons).all()
    p_dct = {}
    for person in persons:
        p_dct.update({person.p_name:person.p_type})

    return p_dct

def get_rooms():
    rooms = SESSIONS.query(Rooms).all()
    r_dct = {}
    for room in rooms:
        r_dct.update({room.r_name:room.r_type})

    return r_dct

def get_allocations():
    allocations = SESSIONS.query(Allocations).all()
    al_dct = {}
    for allocation in allocations:
        al_dct.update({allocation.p_name:[allocation.o_name, allocation.ls_name]})

    return al_dct


def add_person(person_name, person_type):
    ''' Adding a person to database'''
    newperson = Persons(p_name=person_name, p_type=person_type)
    SESSIONS.add(newperson)
    SESSIONS.commit()

def add_room(room_name, room_type, room_capacity):
    ''' Adding a room to database'''
    newuser = Rooms(r_name=room_name, r_type=room_type, r_capacity=room_capacity)
    SESSIONS.add(newuser)
    SESSIONS.commit()

def allocate_room(room_name, person_type):
    ''' Adding a person to database'''
    newallocation = sessions.query(Rooms).filter_by(r_name = room_name).one()
    newallocation.r_occupied +=1
    SESSIONS.add(newpallocation)
    SESSIONS.commit()

def add_allocation(person_name, office_name, livingspace_name):
    ''' Updating allocations table '''
    new_allocation = Allocations(p_name=person_name, o_name=office_name, ls_name=livingspace_name)
    SESSIONS.add(new_allocation)
    SESSIONS.commit()

def edit_allocation(p_name, office_name, livingspaces_name):
    relocation = sessions.query(Rooms).filter_by(p_name = p_name).one()
    relocation.o_name = office_name
    relocation.ls_name = livingspaces_name
