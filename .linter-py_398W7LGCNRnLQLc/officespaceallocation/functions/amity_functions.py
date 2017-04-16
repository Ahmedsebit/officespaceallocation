""" Import module for random item selection"""
import os
import random
from termcolor import colored, cprint
from models.amity_models import Amity
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_person_models import Person, Fellow, Staff
from database.database_functions import Amity_database

class AmityControls(object):
    """ Class AmityControls creation"""

    def __init__(self):
        self.people = []
        self.amity = Amity()
        self.rooms = self.amity.all_rooms
        self.persons = self.amity.all_persons
        self.status = 0

    def load_state(self):
        try:
            self.load_database()
        except:
            return 'Database Error'
        else:
            self.status = 1


    def create_room(self, room_name, room_type):
        h = [x.room_name for x in self.rooms]
        if room_name.upper() in h:
            return 'Room exists'
        else:
            if room_type.upper() == 'OFFICE':
                room = Office(room_name.upper())
                self.rooms.append(room)
                print ('Room succesfully created')
            elif room_type.upper() == 'LIVING SPACE':
                room = LivingSpace(room_name.upper())
                self.rooms.append(room)
                print ('Room succesfully created')
            else:
                print ('Invalid room type')


    def add_person(self, fname, lname, role, accom):
        name = fname+ " "+lname
        n = [x.person_name for x in self.persons]
        if role.upper() == 'FELLOW':
            if name in n:
                return 'The person already exists'
            else:
                fellow = Fellow(name)
                self.persons.append(fellow)
                self.allocate_room(fellow, role, accom)
                print ('Person Succesfully Added')
        elif role.upper() == 'STAFF':
            if name in n:
                print ('The person already exists')
            else:
                staff = Staff(name.upper())
                self.persons.append(staff)
                self.allocate_room(staff, role, accom)
                print ('STAFF succesfully added')
        elif role != 'STAFF' or role != 'FELLOW':
            print ('Wrong person type, should be FELLOW or STAFF')


    def allocate_room(self, person, role, accom):
        offices = [x for x in self.rooms if x.room_type == 'OFFICE'
                   and x.capacity > len(x.occupants)]
        livingspaces = [x for x in self.rooms if x.room_type == 'LIVING SPACE'
                        and x.capacity > len(x.occupants)]

        if len(offices) == 0 and len(livingspaces) == 0:
            return 'No avialable rooms'
        elif len(offices) > 0 and len(livingspaces) == 0:
            office = random.choice(list(offices))
            if role.upper() == 'FELLOW':
                if accom.upper() == 'N':
                    office.occupants.append(person)
                    return 'Fellow allocated office'
                elif accom.upper() == 'Y':
                    office.occupants.append(person)
                    return 'Fellow allocated office. No available living spaces'
                else:
                    office.occupants.append(person)
                    return 'In valid accomodation choice. Fellow allocated office'
            elif role.upper() == 'STAFF':
                if accom.upper() == 'N':
                    office.occupants.append(person)
                    return 'Person allocated room'
                elif accom.upper() == 'Y':
                    office.occupants.append(person)
                    return 'Person allocated office, cannot allocate staff a living space'
                else:
                    return 'Invalid choice'
            else:
                return 'Invalid role. Person not created'

        elif len(offices) == 0 and len(livingspaces) > 0:
            livingspace = random.choice(list(livingspaces))
            if role.upper() == 'FELLOW':
                if accom.upper() == 'N':
                    return 'Fellow not allocated office. No available offices'
                elif accom.upper() == 'Y':
                    livingspace.occupants.append(person)
                    return 'Fellow allocated living space. No available office'
                else:
                    return 'In valid accomodation choice. Fellow not allocated room'
            elif role.upper() == 'STAFF':
                if accom.upper() == 'N':
                    return 'Staff not allocated office. No available offices'
                elif accom.upper() == 'Y':
                    return 'Staff not allocated office. No available offices'
                else:
                    return 'Invalid choice'
            else:
                return 'Invalid role. Person not created'

        elif len(offices) > 0 and len(livingspaces) > 0:
            office = random.choice(list(offices))
            livingspace = random.choice(list(livingspaces))
            if role.upper() == 'FELLOW':
                if accom.upper() == 'N':
                    office.occupants.append(person)
                    return 'Fellow allocated room'
                elif accom.upper() == 'Y':
                    office.occupants.append(person)
                    livingspace.occupants.append(person)
                    return 'Fellow allocated room'
                else:
                    return 'In valid accomodation choice. Fellow not allocated'
            elif role.upper() == 'STAFF':
                if accom.upper() == 'N':
                    office.occupants.append(person)
                    return 'Person allocated room'
                elif accom.upper() == 'Y':
                    office.occupants.append(person)
                    return 'Person allocated office, cannot allocate staff a living space'
                else:
                    return 'Invalid choice'
            else:
                return 'Invalid role. Person not created'



    def relocate_person(self, fname, lname, room_name):
        name = fname + " " +lname
        all_people_names = [person.person_name for person in self.persons]
        if name in all_people_names:
            for room in self.rooms:
                person_list = [person.person_name for person in room.occupants]
                input_room = [room for room in self.rooms if room.room_name == room_name]
                if name in person_list:
                    relocated_person = [person for person in room.occupants if person.person_name == name]
                    if input_room[0].capacity > len(input_room[0].occupants) and input_room[0].room_type == room.room_type:
                        input_room[0].occupants.append(relocated_person[0])
                        room.occupants.remove(relocated_person[0])
                        return 'The person was allocated succesfully'
                    else:
                        return 'The person was not allocated'
        else:
            return 'Person doesnt exist'



    def load_people(self, text_input):
        try:
            myfile = open(text_input, 'r')
        except IOError:
            return 'Input Error'
        except OSError:
            return "OS error"
        except IndexError:
            raise 'Invalid file'
        else:
            for line in myfile:
                item = line.split()
                if len(item) == 4:
                    self.add_person(item[0], item[1], item[2], item[3])
                elif len(item) == 3:
                    self.add_person(item[0], item[1], item[2], 'N')
                else:
                    return 'Invalid file'




    def print_room(self, room_name):
        """ Printing room function """
        room_names = [room.room_name for room in self.rooms]
        if room_name in room_names:
            selected_room = [room for room in self.rooms if room.room_name == room_name]
            people = [person.person_name for person in selected_room[0].occupants]
            print(selected_room[0].room_name)
            print(people)


    def load_database(self):
        amity_database = Amity_database()
        allocation_list = amity_database.get_allocations()
        room_list = amity_database.get_rooms()
        person_list = amity_database.get_persons()

        for key in room_list:
            room_name = key
            room_type = room_list[key]
            self.create_room(room_name, room_type)

        for key in person_list:
            name = key
            person_type = person_list[key]
            if person_type.upper() == 'STAFF':
                staff = Staff(name)
                self.persons.append(staff)
            elif person_type.upper() == 'FELLOW':
                fellow = Fellow(name)
                self.persons.append(fellow)


        for key in allocation_list:
            name = key
            room = allocation_list[key]
            allocated_person = [person for person in self.persons if person.person_name == name]
            office = room[0]
            livingspace = room[1]
            allocated_office = [room for room in self.rooms if room.room_name == office]
            allocated_livingspace = [room for room in self.rooms if room.room_name == livingspace]
            if allocated_livingspace != []:
                allocated_office[0].occupants.append(Fellow(name))
                allocated_livingspace[0].occupants.append(Fellow(name))
            else:
                office = room[0]
                allocated_office = [room for room in self.rooms if room.room_name == office]
                allocated_office[0].occupants.append(Fellow(name))


    def save_database(self):
        amity_database = Amity_database()
        all_allocation = {}
        for room in self.rooms:
            for person in room.occupants:
                all_allocation.update({person.person_name:['','']})


        for room in self.rooms:
            for person in room.occupants:
                if room.room_type == "OFFICE":
                    all_allocation[person.person_name][0] = room.room_name
                elif room.room_type == "LIVING SPACE":
                    all_allocation[person.person_name][1] = room.room_name



        rooms_in_db = amity_database.get_rooms()
        for room in self.rooms:
            if room.room_name not in rooms_in_db:
                amity_database.add_room(room.room_name, room.room_type, room.capacity)

        persons_in_db = amity_database.get_persons()
        for person in self.persons:
            if person.person_name not in persons_in_db:
                amity_database.add_person(person.person_name, person.person_type)


        allocations_in_db = amity_database.get_allocations()


        for person in all_allocation:
            if person in allocations_in_db:
                amity_database.update_allocation(person, all_allocation[person][0], all_allocation[person][1])
            else:
                amity_database.add_allocation(person, all_allocation[person][0], all_allocation[person][1])

    def save_state(self):
        try:
            self.save_database()
        except:
            return 'Database Error'
        else:
            return'System state saved'
