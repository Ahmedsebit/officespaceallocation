from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database_models import Persons, Rooms, Allocations, BASE

ENGINE = create_engine('sqlite:///amity.db')
BASE.metadata.create_all(ENGINE)
DBSESSION = sessionmaker(bind=ENGINE)
SESSIONS = DBSESSION()

class AmityDatabase(object):
    '''
    This class contains functions hwich are used for database
    functions.
    '''

    def get_persons(self):
        persons = SESSIONS.query(Persons).all()
        person_dictionary = {}
        for person in persons:
            person_dictionary.update({person.person_name:person.person_type})
        return person_dictionary

    def get_rooms(self):
        rooms = SESSIONS.query(Rooms).all()
        room_dictionary = {}
        for room in rooms:
            room_dictionary.update({room.room_name:room.room_type})
        return room_dictionary

    def get_allocations(self):
        allocations = SESSIONS.query(Allocations).all()
        allocation_dictionary = {}
        for allocation in allocations:
            allocation_dictionary.update({allocation.person_name:
                                          [allocation.office_name, allocation.livingspace_name]})
        return allocation_dictionary


    def add_person(self, person_name, person_type):
        ''' Adding a person to database'''
        newperson = Persons(person_name=person_name, person_type=person_type)
        SESSIONS.add(newperson)
        SESSIONS.commit()

    def add_room(self, room_name, room_type, room_capacity):
        ''' Adding a room to database'''
        newuser = Rooms(room_name=room_name, room_type=room_type, room_capacity=room_capacity)
        SESSIONS.add(newuser)
        SESSIONS.commit()


    def add_allocation(self, person_name, office_name, livingspace_name):
        ''' Updating allocations table '''
        new_allocation = Allocations(person_name=person_name,
                                     office_name=office_name, livingspace_name=livingspace_name)
        SESSIONS.add(new_allocation)
        SESSIONS.commit()

    def update_allocation(self, person_name, office_name, livingspace_name):
        ''' Updating allocations table '''
        person = SESSIONS.query(Allocations).filter_by(person_name=person_name).one()
        person.office_name = office_name
        person.livingspace_name = livingspace_name
        SESSIONS.add(person)
        SESSIONS.commit()
