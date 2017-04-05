""" Import module for random item selection"""
import random


class AmityControls(object):
    """ Class AmityControls creation"""
    def __init__(self):
        self.all_persons = {"Ahmed Yusuf":"Fellow", "Yusuf":"Staff", "T MK":"Fellow"}
        self.all_rooms = {"Kigali":"Office", "Krypton":"Living Space", "Kampala":"Office",
                          "Gotham":"Living Space"}
        self.all_allocations = {"Ahmed Yusuf":["Kigali", "Krypton"], "Yusuf Sebit":["Kampala"],
                                "T MK":["Kampala", "Gotham"]}
        self.amity = {}


    def load_state():
        """ Loading state function """
        pass


    def create_room(self, room_name, room_type):
        """ Room creation function"""
        self.all_rooms.update({room_name:room_type})


    def add_person(self, fname, lname, role, accom):
        """ Add and allocate person function """
        name = fname+ " "+lname
        self.all_persons.update({name:role})
        offices = {k: v for k, v in self.all_rooms.items() if v == "Office"}
        livingspaces = {k: v for k, v in self.all_rooms.items() if v == "Living Space"}
        office = random.choice(list(offices))
        livingspace = random.choice(list(livingspaces))
        if accom == 'Y' and role == 'Fellow':
            self.all_allocations.update({name:[office, livingspace]})
        elif accom == 'N' and role == 'Fellow':
            self.all_allocations.update({name: [office]})
        elif role == 'Staff':
            self.all_allocations.update({name: [office]})

    def relocate_office(self, fname, lname, reloc_type, room_name):
        """ Rellocate person function """
        #person = fname + " " + lname
        #self.all_allocations[person][1] = room_name
        pass

    def load_people(self, text_input):
        """ Load and relocate person function """
        myfile = open(text_input, 'r')
        count = 0
        for line in myfile:
            item = line.split()
            self.add_person(item[0], item[1], item[2], item[3])
            count += 1
        return self.all_allocations


    def print_room(self, name):
        """ Printing room function """
        selected_room = {k: v for k, v in self.all_allocations.items() if v[0] == name}
        return selected_room
