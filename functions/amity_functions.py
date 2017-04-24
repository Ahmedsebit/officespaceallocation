""" Import module for random item selection"""
import os
import random
from termcolor import colored, cprint
from models.amity_models import Amity
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_person_models import Person, Fellow, Staff
from database.database_functions import AmityDatabase

class AmityControls(object):

    """ This class contains amity functionality """

    def __init__(self):
        self.people = []
        self.amity = Amity()
        self.rooms = self.amity.all_rooms
        self.persons = self.amity.all_persons
        self.status = 0


    def load_state(self, filename):

        '''
        This function loads the allocation application with data fom database
        The function calls load_database function which query data from the database
        and adds the data to the various lists in the application
        '''
        file_type = filename.split(".")
        if len(file_type) == 2:
            if file_type[1] == 'db':
                self.load_database(filename)
                return 'Loading state succesfull'
            else:
                return 'Loading state failed. Wrong file type'
        else:
            return 'Loading state failed. File type error'


    def create_room(self, room_name, room_type):
        '''
        This function creates room with respest to the room type.
        The room is only created if the room does not exist and it has a valid room type
        '''
        # creating a list of all room names to check if the room already exists
        all_rooms = [room.room_name for room in self.rooms]
        if room_name.upper() in all_rooms:
            return 'Room exists'
        else:
            if room_type.upper() == 'OFFICE':
                room = Office(room_name.upper())
                self.rooms.append(room)
                return room.room_name + ' office succesfully created'
            elif room_type.upper() == 'LIVINGSPACE':
                room = LivingSpace(room_name.upper())
                self.rooms.append(room)
                return room.room_name + ' living space succesfully created'
            else:
                # if invalid room type was submitted
                return 'Invalid room type'


    def add_person(self, first_name, last_name, role, want_accommodation='N'):
        '''
        This functions adds person to the datase.
        The erson is added and allocated a room by calling the office_allocation
        or livingspace_allocation with repect to the eprson type and the choice for
        accomodation.
        '''
        # creating a list of all people names to check if the person already exists
        all_persons_names = [person.person_name for person in self.persons]
        name = first_name+ " "+last_name
        role = role.upper()
        if name in all_persons_names:
            return 'The person already exists'
        else:
            if role.upper() == 'FELLOW' and want_accommodation == 'N':
                fellow = Fellow(name)
                self.persons.append(fellow)
                self.allocate_office(fellow, fellow.person_type)
                return fellow.person_name + ' succesfully added'
            elif role.upper() == 'FELLOW' and want_accommodation == 'Y':
                fellow = Fellow(name)
                fellow.want_accommodation = 'Y'
                self.persons.append(fellow)
                self.allocate_office(fellow, fellow.person_type)
                self.allocate_livingspace(fellow, fellow.person_type)
                return fellow.person_name+' succesfully added'
            elif role.upper() == 'STAFF' and want_accommodation == 'N':
                staff = Staff(name)
                self.persons.append(staff)
                self.allocate_office(staff, staff.person_type)
                return staff.person_name+' succesfully added'
            elif role.upper() == 'STAFF' and want_accommodation == 'Y':
                staff = Staff(name)
                self.persons.append(staff)
                self.allocate_office(staff, staff.person_type)
                return staff.person_name+' succesfully Added to Office. Cannot allocate staff a livingspace'
            elif role.upper() != 'STAFF' and role.upper() != 'FELLOW':
                # if role is not STAFF or FELLOW
                return 'Invalid role. Person not created'
            else:
                return 'Invalid choice'



    def allocate_office(self, person, role):
        '''
        This function is used to allocate an office.
        It checks if there is an office, then checks for a random office
        with a if there is a vacant space.
        '''
        # creating a list of all offices with available spaces
        offices = [room for room in self.rooms if room.room_type == 'OFFICE'
                   and room.capacity > len(room.occupants)]
        # If there is no available space in both office
        if len(offices) == 0:
            return 'No aviallable offices'
        # If there is available office
        elif len(offices) > 0:
            office = random.choice(list(offices))
            if role.upper() == 'FELLOW':
                office.occupants.append(person)
                return person.person_name+ ' added and allocated '+ office.room_name
            elif role.upper() == 'STAFF':
                office.occupants.append(person)
                return person.person_name+ ' added and allocated '+office.room_name
            else:
                return 'Invalid role. Person not created'


    def new_allocate_office(self, person_name):
        '''
        This function is used to allocate an office.
        It checks if there is an office, then checks for a random office
        with a if there is a vacant space.
        '''
        offices = [room for room in self.rooms if room.room_type == 'OFFICE']
        person_in_offices = []
        # creating a list of all offices with available spaces
        persons_in_system = [person.person_name for person in self.persons]
        if person_name in persons_in_system:
            person = [person for person in self.persons if person.person_name == person_name]
            for room in offices:
                for person_in_room in room.occupants:
                    person_in_offices.append(person_in_room)
            if person[0] in person_in_offices:
                return 'Person already allocated an office'
            else:
                self.allocate_office(person[0], person[0].person_type)
                return 'The person has been allocated an office'
        else:
            return 'The person does not exist in the system'




    def allocate_livingspace(self, person, role):
        '''
        This function is used to allocate an living space.
        It checks if there is an office, then checks for a living space
        with a if there is a vacant space. It laso checks for the person type
        since STAFF cannot be allocated a living space
        '''
        # creating a list of all offices with available spaces
        livingspaces = [room for room in self.rooms if room.room_type == 'LIVINGSPACE']
        # If there is no available space in both office
        if len(livingspaces) == 0:
            return 'No aviallable living space'
        # If there is available office
        elif len(livingspaces) > 0:
            livingspace = random.choice(list(livingspaces))
            if role.upper() == 'FELLOW':
                livingspace.occupants.append(person)
                return person.person_name+ ' allocated '+livingspace.room_name
            elif role.upper() == 'STAFF':
                return 'Invalid choice, staff cannot be allocated a living space'
            else:
                return 'Invalid role. Person not allocated'



    def new_allocate_livingspace(self, person_name):
        '''
        This function is used to allocate an office.
        It checks if there is an office, then checks for a random office
        with a if there is a vacant space.
        '''
        livingspaces = [room for room in self.rooms if room.room_type == 'LIVINGSPACE']
        person_in_livingspace = []
        # creating a list of all offices with available spaces
        persons_in_system = [person.person_name for person in self.persons]
        if person_name in persons_in_system:
            person = [person for person in self.persons if person.person_name == person_name]
            for room in livingspaces:
                for person_in_room in room.occupants:
                    person_in_livingspace.append(person_in_room)
            if person[0] in person_in_livingspace:
                return 'Person already allocated an office'
            else:
                if person[0].person_type == "STAFF":
                    return 'Staff cannot be allocated a living space'
                else:
                    self.allocate_livingspace(person[0], person[0].person_type)
                    return 'The person has been allocated a living space'
        else:
            return 'The person does not exist in the system'



    def reallocate_person(self, fname, lname, room_name):
        '''
        This function is used to reallocate person from a room they belonged to to a
        specified room. The person is only relocated if they are not already allocated
        the room and if the room has vacancy.
        '''
        name = fname + " " +lname
        room_name = room_name.upper()
        all_people_names = [person.person_name for person in self.persons]
        # cheking if person exists
        if name.upper() in all_people_names:
            for room in self.rooms:
                # getting the rooms the person belong to
                person_list = [person.person_name for person in room.occupants]
                input_room = [room for room in self.rooms if room.room_name == room_name]
                if len(input_room) == 0:
                    return 'the room does not exists'
                else:
                    persons_in_inputroom \
                    = [person.person_name for person in input_room[0].occupants]
                    if name in person_list:
                        reallocated_person = [person for person in room.occupants
                                              if person.person_name == name]
                        if input_room[0].capacity > len(input_room[0].occupants):
                            if input_room[0].room_type == room.room_type:
                                # adding the person to the room
                                if name in persons_in_inputroom:
                                    return "The person already exists in the room"
                                else:
                                    input_room[0].occupants.append(reallocated_person[0])
                                    # removing the person from the previous room
                                    room.occupants.remove(reallocated_person[0])
                                    return reallocated_person[0].person_name+'  was reallocated succesfully from '+room.room_name +' to '+input_room[0].room_name
                            else:
                                return 'The person was not reallocated. The person has not been allocated this room type'
                        else:
                            return 'The selected room is full'
        else:
            return 'Person doesnt exist'



    def unallocations(self, file_name):
        '''
        This function is used to create an file that has all unallocations.
        This function is later used by print_unallocations functions to print all
        unallocated persons.
        '''
        person_name_list = [person.person_name for person in self.persons]
        person_in_room = []
        unallocated_persons = []
        for room in self.rooms:
            for person in room.occupants:
                person_in_room.append(person.person_name)

        file = open(file_name, 'w')
        for person in person_name_list:
            if person not in person_in_room:
                unallocated_persons.append(person)
                file.write(person + "\n")
                file.write('-------------------------------------------------'+ "\n")
                file.write(' '+ "\n")
        file.close()


    def list_unallocations(self):
        '''
        This function is used to create alist that has all unallocations.
        '''
        person_name_list = [person.person_name for person in self.persons]
        person_in_room = []
        unallocated_persons = []
        for room in self.rooms:
            for person in room.occupants:
                person_in_room.append(person.person_name)

        for person in person_name_list:
            if person not in person_in_room:
                unallocated_persons.append(person)

        if len(person_name_list) == 0:
            cprint('There are no person in the system', 'yellow')
        elif len(unallocated_persons) == 0:
            cprint('Everyone has been allocated a room', 'yellow')
        else:
            for person in unallocated_persons:
                cprint(person, 'green')




    def print_unallocations(self, file_name):
        '''
        This functions is used to print all unallocations.
        The functions calls the unallocations functions which creates the file.
        This function checks for the correct file output.
        '''
        # adding person from all rooms to allocation dictionary
        person_name_list = [person.person_name for person in self.persons]
        person_in_room = []
        unallocated_persons = []
        for room in self.rooms:
            for person in room.occupants:
                person_in_room.append(person.person_name)

        for person in person_name_list:
            if person not in person_in_room:
                unallocated_persons.append(person)

        if len(person_name_list) == 0:
            return 'There are no people in the system'
        elif len(unallocated_persons) == 0:
            return 'Every person has been allocated a room'
        else:
            file_type = file_name.split(".")
            if len(file_type) == 2:
                if file_type[1] == 'txt':
                    self.unallocations(file_name)
                    return "Unallocated persons printed to :"+file_name
                else:
                    return 'Invalid file type'
            else:
                return 'Invalid file'



    def list_allocations(self):
        '''
        This function is used to create an list that has all allocations.
        '''
        # adding person from all rooms to allocation dictionary
        person_name_list = [person.person_name for person in self.persons]
        person_in_room = []
        for room in self.rooms:
            for person in room.occupants:
                person_in_room.append(person.person_name)
        if len(person_name_list) == 0:
            cprint('There are no person in the system', 'yellow')
        elif len(person_in_room) == 0:
            cprint('There are no people in the rooms', 'yellow')
        else:
            for room in self.rooms:
                people = [person.person_name for person in room.occupants]
                cprint(room.room_name,  'green')
                print ('-------------------------------------------------')
                cprint(people, 'green')
                print("")


    def allocations(self, file_name):
        '''
        This function is used to create an file that has all allocations.
        This function is later used by print_allocations functions to print all
        allocated persons.
        '''
        # adding person from all rooms to allocation dictionary
        file = open(file_name, 'w')
        for room in self.rooms:
            file.write(room.room_name + "\n")
            file.write('-------------------------------------------------'+ "\n")
            file.write(str([person.person_name for person in room.occupants])+ "\n")
            file.write(' '+ "\n")
            file.write(' '+ "\n")
        file.close()


    def print_allocations(self, file_name):
        '''
        This functions is used to print all allocations.
        The functions calls the allocations functions which creates the file.
        This function checks for the correct file output.
        '''
        person_name_list = [person.person_name for person in self.persons]
        person_in_room = []
        for room in self.rooms:
            for person in room.occupants:
                person_in_room.append(person.person_name)

        if len(person_name_list) == 0:
            return 'There are no person in the system'
        elif len(person_in_room) == 0:
            return 'There are no people in the rooms'
        else:
            file_type = file_name.split(".")
            if len(file_type) == 2:
                if file_type[1] == 'txt':
                    self.allocations(file_name)
                    return 'Allocations printed to :'+file_name
                else:
                    return 'Invalid file type'
            else:
                return 'Invalid file'



    def load_people(self, text_input):
        '''
        This functions is used to load the application with persons in a text file.
        This function checks for the correct file input and call the add_person
        function to add the persons in the application.
        '''
        try:
            # Opening the text file
            myfile = open(text_input, 'r')
        except:
            return 'Invalid file'
        else:
            for line in myfile:
                item = line.split()
                if len(item) == 4:
                    # adding the person to the system if accomodation is edited
                    self.add_person(item[0], item[1], item[2], item[3])
                elif len(item) == 3:
                    # dding the person to the system if accomodation is not edited
                    self.add_person(item[0], item[1], item[2], 'N')
                else:
                    return 'Invalid file'
            return 'People loaded succesfully'


    def print_room(self, room_name):
        """
        This function is used to print a room and its occupants.
        The function checks if the room exists
        """
        room_names = [room.room_name for room in self.rooms]
        # cheking if the room exists
        if room_name in room_names:
            selected_room = [room for room in self.rooms if room.room_name == room_name]
            people = [person.person_name for person in selected_room[0].occupants]
            return selected_room[0].room_name + '\n'+str(people)
        else:
            return 'Room does not exist'


    def load_database(self, filename):
        '''
        The functions get the data from a database and add the data to the amity system.
        If the database doesn't exist, it creates a new database. The function queries
        the database through database functions in the database function files.
        The function then adds the data to the the amity system through creating
        rooms in terms of room types and person with regards to person types
        '''
        amity = AmityDatabase()
        people = amity.get_persons(filename)
        rooms = amity.get_rooms(filename)
        allocations = amity.get_allocations(filename)
        all_people_name = [person.person_name for person in self.persons]
        all_room_name = [room.room_name for room in self.rooms]

        for person in people:
            if person not in all_people_name:
                if people[person] == 'STAFF':
                    self.persons.append(Staff(person))
                elif people[person] == 'FELLOW':
                    self.persons.append(Fellow(person))

        for room in rooms:
            if room not in all_room_name:
                if rooms[room] == 'OFFICE':
                    self.rooms.append(Office(room))
                elif rooms[room] == 'LIVINGSPACE':
                    self.rooms.append(LivingSpace(room))


        for request_person in allocations:
            room = allocations[request_person]
            office = room[0]
            livingspace = room[1]
            person_cl = [person for person in self.persons if person.person_name == request_person]
            if livingspace != '':
                allocated_office = [room for room in self.rooms if room.room_name == office]
                persons_in_allocatedoffice = [person.person_name
                                              for person in allocated_office[0].occupants]
                allocated_livingspace = [room for room
                                         in self.rooms if room.room_name == livingspace]
                persons_in_allocatedlivingspace = [person.person_name
                                                   for person in allocated_livingspace[0].occupants]
                if request_person not in persons_in_allocatedoffice:
                    allocated_office[0].occupants.append(person_cl[0])
                if request_person not in persons_in_allocatedlivingspace:
                    allocated_livingspace[0].occupants.append(person_cl[0])
            else:
                allocated_office = [room for room in self.rooms if room.room_name == office]
                persons_in_allocatedoffice = [person.person_name
                                              for person in allocated_office[0].occupants]
                if request_person not in persons_in_allocatedoffice:
                    allocated_office[0].occupants.append(person_cl[0])


    def save_database(self, filename):
        '''
        The functions saves the data from a database with data from the amity system.
        If the database doesn't exist, it creates a new database.
        The function loads the database through with rooms in terms of room types and
        person with regards to person types. The function also add the database with the
        room the person belong to.
        '''
        amity_database = AmityDatabase()
        all_allocation = {}

        # adding person from all rooms to allocation dictionary
        for room in self.rooms:
            for person in room.occupants:
                all_allocation.update({person.person_name:[person.person_type, '', '']})

        # adding person's office and living space to the all alocation's dictionary
        for room in self.rooms:
            for person in room.occupants:
                if room.room_type == "OFFICE":
                    all_allocation[person.person_name][1] = room.room_name
                elif room.room_type == "LIVINGSPACE":
                    all_allocation[person.person_name][2] = room.room_name

        # adding new rooms to database
        rooms_in_db = amity_database.get_rooms(filename)
        for room in self.rooms:
            if room.room_name not in rooms_in_db:
                amity_database.add_room(filename, room.room_name, room.room_type)


        # adding data to the allocations table in database
        person_in_db = amity_database.get_allocations(filename)
        for person in all_allocation:
            if person in person_in_db:
                amity_database.update_person(filename, person,
                                             all_allocation[person][1], all_allocation[person][2])
            else:
                amity_database.add_person(filename, person, all_allocation[person][0],
                                          all_allocation[person][1], all_allocation[person][2])

    def save_state(self, filename):
        '''
        The functions saves the data from a database by calling the save_database function.
        The function checks for the valid data file name and type provided
        then creates the database if it doesn't exists or updates an existing database
        '''
        file_type = filename.split(".")
        if len(file_type) == 2:
            if file_type[1] == 'db':
                self.save_database(filename)
                return 'State saved'
            else:
                return 'Saving state failed. Wrong file type'
        else:
            return 'Saving state failed. File type error'
