""" Import module for random item selection"""
import os
import random
from models.amity_models import Amity
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_person_models import Person, Fellow, Staff

class AmityControls(object):
    """ Class AmityControls creation"""

    def __init__(self):
        self.people = []
        self.amity = Amity()
        self.rooms = self.amity.all_rooms
        self.persons = self.amity.all_persons

    def load_state(self):
        return 'System loaded'

    def create_room(self, room_name, room_type):
        h = [x.room_name for x in self.rooms]
        if room_name.upper() in h:
            return 'Room exists'
        else:
            if room_type.upper() == 'OFFICE':
                self.rooms.append(Office(room_name.upper()))
                return 'Room succesfully created'
            elif room_type.upper() == 'LIVING SPACE':
                self.rooms.append(LivingSpace(room_name.upper()))
                'Room succesfully created'
            else:
                return 'Invalid room type'


    def add_person(self, fname, lname, role, accom):
        name = fname+ " "+lname
        n = [x.person_name for x in self.persons]
        if role.upper() == 'FELLOW':
            if name in n:
                return 'The person already exists'
            else:
                self.persons.append(Fellow(name.upper()))
                # self.allocate_room(name, role, accom)
                return 'Person Succesfully Added'
        elif role.upper() == 'STAFF':
            if name in n:
                self.persons.append(Staff(name.upper()))
                # self.allocate_room(name, role, accom)
                return 'STAFF succesfully added'
        elif role != 'STAFF' or role != 'FELLOW':
            return 'Wrong person type, should be FELLOW or STAFF'
        allocate_room(name, rome, accom)


    def allocate_room(self, name, role, accom):
        offices = [x for x in self.rooms if x.room_type == 'OFFICE'
                   and x.capcity > len(x.occupants)]
        livingspaces = [x for x in self.rooms if x.room_type == 'LIVING SPACE'
                        and x.capcity > len(x.occupants)]
        if len(office) < 1 and len(livingspaces) < 1:
            return 'No rooms are available'
        elif len(office) > 1 and len(livingspace) < 1:
            return 'No living spaces are available'
            office = random.choice(list(offices))
            if role == 'FELLOW':
                office.occupants.append(Fellow(name.upper()))
                return 'Office and Living Space succesfully allocated'
            elif role == 'STAFF':
                office.occupants.append(Staff(name.upper()))
                return 'Office Succesfully allocated. Cannot allocate staff a living space'
        elif len(office) < 1 and len(livingspace) < 1:
            return 'No offices are available'
            livingspace = random.choice(list(livingspaces))
            if role == 'FELLOW':
                if accom == 'Y':
                    livingspace.occupants.append(Fellow(name.upper()))
                    return 'Living Space succesfully allocated'
            elif role == 'STAFF':
                return 'Cannot allocate staff a living space'
        else:
            office = random.choice(list(offices))
            livingspace = random.choice(list(livingspaces))
            if role == 'FELLOW':
                if accom == 'Y':
                    office.occupants.append(Fellow(name.upper()))
                    livingspace.occupants.append(Fellow(name.upper()))
                    return 'Office and Living Space succesfully allocated'
                elif accom == 'N':
                    office.occupants.append(Fellow(name.upper()))
                return 'Office succesfully allocated'
            elif role == 'STAFF':
                if accom == 'Y':
                    office.occupants.append(Staff(name.upper()))
                    return 'Office Succesfully allocated. Cannot allocate staff a living space'
                else:
                    office.occupants.append(Staff(name.upper()))
                    return 'STAFF succesfully allocated'
            elif role != 'STAFF' or role != 'FELLOW':
                return 'Invalid person role'


    def relocate_office(self, fname, lname, reloc_type, room_name):
        name = fname + " " +lname
        n = [x.person_name for x in self.persons]
        if name in n:
            if reloc_type == 'OFFICE':
                self.all_allocations[name][0] = room_name
                return 'Relocation succesful'
            elif reloc_type == 'LIVING SPACE':
                self.all_allocations[name][1] = room_name
                return 'Relocation succesful'
            else:
                return 'wrong room type. Should be OFFICE  or LIVING SPACE'
        elif name in self.all_staff:
            if reloc_type == 'LIVING SPACE':
                return 'Cannot Allocate Staff to a living Space'
            elif reloc_type == 'OFFICE':
                self.all_allocations[name][0] = room_name
                return 'Relocation succesful'
            else:
                return 'wrong room type. Should be OFFICE  or LIVING SPACE'
        else:
            return 'The person does not exists'


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
                self.add_person(item[0], item[1], item[2], item[3])
            return 'Loading succesful'




    def print_room(self, name):
        """ Printing room function """
        if name in self.all_offices or name in all_livingspaces:
            selected_room = {k: v for k, v in self.all_allocations.items() if v[0] == name}
            return selected_room
        else:
            return 'Wrong room name'
