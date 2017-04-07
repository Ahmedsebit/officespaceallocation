""" Import module for random item selection"""
import os
import random
from models.amity_models import Amity, Office, LivingSpace, Person, Fellow, Staff

class AmityControls(object):
    """ Class AmityControls creation"""
    def __init__(self):

        self.office = Office()
        self.livingspace = LivingSpace()
        self.amity = Amity()
        self.fellows = Fellow()
        self.staff = Staff()
        self.all_fellows = self.fellows.all_Fellows
        self.all_staff = self.staff.all_Staff
        self.all_allocations = self.amity.all_allocations
        self.all_offices = self.office.all_Offices
        self.all_livingspaces = self.livingspace.all_Livingspaces

    def load_state(self):
        """ Loading state function """
        pass


    def create_room(self, room_name, room_type):
        """ Room creation function"""
        if room_type == 'OFFICE':
            if room_name in self.all_offices:
                return 'Room already exists'
            else:
                self.all_offices.update({room_name:0})
                return 'Room succefully created'
        elif room_type == 'LIVING SPACE':
            if room_name in self.all_livingspaces:
                return 'Room already exists'
            else:
                self.all_livingspaces.update({room_type:0})
                return 'Room succefully created'
        else:
            return 'Invalid room type, Should be OFFICE or LIVING SPACE'


    def add_person(self, fname, lname, role, accom):
        """ Add and allocate person function """
        name = fname+ " "+lname
        office = random.choice(list(self.all_offices))
        livingspace = random.choice(list(self.all_livingspaces))
        if role == 'FELLOW':
            if name in self.all_fellows:
                return 'The person already exists'
            else:
                self.all_fellows.append(name)
                return 'Person Succesfully Added'
        elif role == 'STAFF':
            self.all_staff.append(name)
            return 'STAFF succesfully added'
        elif role != 'STAFF' or role != 'FELLOW':
            return 'Wrong person type, should be FELLOW or STAFF'
        allocate_room(self, name, role, accom)

    def allocate_room(self, name, role, accom):
        office = random.choice(list(self.all_offices))
        livingspace = random.choice(list(self.all_livingspaces))
        if role == 'FELLOW':
            if accom == 'Y':
                self.all_allocations.update({name:[office, livingspace]})
                return 'Office and Living Space succesfully allocated'
            elif accom == 'N':
                self.all_allocations.update({name:[office]})
            return 'Office succesfully allocated'
        elif role == 'STAFF':
            if accom == 'Y':
                self.all_allocations.update({name:[office]})
                return 'Office Succesfully allocated. Cannot allocate staff a living space'
            else:
                self.all_allocations.update({name:[office]})
                return 'STAFF succesfully allocated'
        elif role != 'STAFF' or role != 'FELLOW':
            return 'Invalid person role'
        pass


    def relocate_office(self, name, reloc_type, room_name):
        """ Rellocate person function """

        if name in self.all_fellows:
            if reloc_type == 'OFFICE':
                self.all_allocations[name][0] = room_name
                return 'Relocation succesful'
            elif reloc_type == 'LIVING SPACE':
                self.all_allocations[person][1] = room_name
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
        """ Load and relocate person function """
        try:
            myfile = open(text_input, 'r')
            for line in myfile:
                item = line.split()
                if len(item) < 1:
                    return 'Loading Failed, empty file'
                elif len(item) < 4 or len(item) > 4:
                    return 'Loading Failed, Invalid failed'
                else:
                    self.add_person(item[0], item[1], item[2], item[3])
        except Exception as e:
            raise OSError


    def print_room(self, name):
        """ Printing room function """
        if name in self.all_offices or name in all_livingspaces:
            selected_room = {k: v for k, v in self.all_allocations.items() if v[0] == name}
            return selected_room
        else:
            return 'Wrong room name'
