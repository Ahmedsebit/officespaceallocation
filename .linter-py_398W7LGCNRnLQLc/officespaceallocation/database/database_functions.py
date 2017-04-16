from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database_models import Persons, Rooms, Allocations, BASE

ENGINE = create_engine('sqlite:///database/amity.db')

BASE.metadata.create_all(ENGINE)
DBSESSION = sessionmaker(bind=ENGINE)
SESSIONS = DBSESSION()

class Amity_database(object):

    def get_persons(self):
        persons = SESSIONS.query(Persons).all()
        p_dct = {}
        for person in persons:
            p_dct.update({person.p_name:person.p_type})

        return p_dct

    def get_rooms(self):
        rooms = SESSIONS.query(Rooms).all()
        r_dct = {}
        for room in rooms:
            r_dct.update({room.r_name:room.r_type})

        return r_dct

    def get_allocations(self):
        allocations = SESSIONS.query(Allocations).all()
        al_dct = {}
        for allocation in allocations:
            al_dct.update({allocation.p_name:[allocation.o_name, allocation.ls_name]})

        return al_dct


    def add_person(self, person_name, person_type):
        ''' Adding a person to database'''
        newperson = Persons(p_name=person_name, p_type=person_type)
        SESSIONS.add(newperson)
        SESSIONS.commit()

    def add_room(self, room_name, room_type, room_capacity):
        ''' Adding a room to database'''
        newuser = Rooms(r_name=room_name, r_type=room_type, r_capacity=room_capacity)
        SESSIONS.add(newuser)
        SESSIONS.commit()


    def add_allocation(self, person_name, office_name, livingspace_name):
        ''' Updating allocations table '''
        new_allocation = Allocations(p_name=person_name, o_name=office_name, ls_name=livingspace_name)
        SESSIONS.add(new_allocation)
        SESSIONS.commit()

    def update_allocation(self, person_name, office_name, livingspace_name):
        ''' Updating allocations table '''
        person = SESSIONS.query(Allocations).filter_by(p_name=person_name).one()
        person.o_name = office_name
        person.ls_name = livingspace_name
        SESSIONS.add(person)
        SESSIONS.commit()
