from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database_models import Persons, Rooms, BASE



class AmityDatabase(object):

    '''
    class contains function for the database
    '''

    def __init__(self):
        pass

    def initialize(self, filename):
        '''
        The function initaializes the database through a new databse or an existing database.
        '''
        self.ENGINE = create_engine('sqlite:///'+filename)
        BASE.metadata.create_all(self.ENGINE)
        self.DBSESSION = sessionmaker(bind=self.ENGINE)
        self.SESSIONS = self.DBSESSION()

    def get_persons(self, filename):
        '''
        The function get the person from database and return a dictionary with all the people
        in the database
        '''
        self.initialize(filename)
        persons = self.SESSIONS.query(Persons).all()
        person_dictionary = {}
        for person in persons:
            person_dictionary.update({person.person_name:person.person_type})
        return person_dictionary

    def get_rooms(self, filename):
        '''
        The function get the rooms from database and returns a dictionary with the rooms in the
        database with regards to the room name and room type to a dictionary
        '''
        self.initialize(filename)
        rooms = self.SESSIONS.query(Rooms).all()
        room_dictionary = {}
        for room in rooms:
            room_dictionary.update({room.room_name:room.room_type})
        return room_dictionary

    def get_allocations(self, filename):
        '''
        The function get the allocated rooms for each person from database and returns a dictionary
        with regards to person name and person type and the office and living space
        '''
        self.initialize(filename)
        allocations = self.SESSIONS.query(Persons).all()
        allocations_dictionary = {}
        for allocation in allocations:
            allocations_dictionary.update({allocation.person_name:[allocation.office_name,
                                                                   allocation.livingspace_name]})
        return allocations_dictionary

    def add_person(self, filename, person_name, person_type, office_name, livingspace_name):
        '''
        The function is used to add the person to the dictionary
        '''
        self.initialize(filename)
        newperson = Persons(person_name=person_name, person_type=person_type,
                            office_name=office_name, livingspace_name=livingspace_name)
        self.SESSIONS.add(newperson)
        self.SESSIONS.commit()

    def add_room(self, filename, room_name, room_type):
        '''
        The function is used to add the rooms to the dictionary
        '''
        self.initialize(filename)
        newroom = Rooms(room_name=room_name, room_type=room_type)
        self.SESSIONS.add(newroom)
        self.SESSIONS.commit()


    def update_person(self, filename, person_name, office_name, livingspaces_name):
        '''
        The function is used to add the person to the dictionary
        '''
        self.initialize(filename)
        reallocation = self.SESSIONS.query(Persons).filter_by(person_name=person_name).one()
        reallocation.office_name = office_name
        reallocation.livingspace_name = livingspaces_name
        self.SESSIONS.add(reallocation)
        self.SESSIONS.commit()
