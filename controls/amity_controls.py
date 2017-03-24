import sys
import random
sys.path.insert(0, '/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/controls')

class AmityControls():
    def __init__(self):
        self.all_persons = {"Ahmed Yusuf":"Fellow", "Yusuf":"Staff"}
        self.all_rooms = {"Kigali":"Office","Krypton":"Living Space","Kampala":"Office","Gotham":"Living Space"}
        self.all_allocations = {"Ahmed Yusuf":["Kigali","Krypton"],"Yusuf":["Kampala"]}

    def add_person(self, fname, lname, role, accom):
        name = fname+ " "+lname
        self.all_persons.update({name:role})
        offices = {k: v for k, v in self.all_rooms.items() if v == "Office"}
        livingspaces = {k: v for k, v in self.all_rooms.items() if v == "Living Space"}
        office = random.choice(list(offices))
        livingspace = random.choice(list(livingspaces))
        self.all_allocations.update({name:[office,livingspace]})


    def create_room(self, room_name, room_type):
        self.all_rooms.update({room_name:room_type})
        pass

    def relocate_office(self, fname, lname ,reloc_type, room_name ):
        person = fname + " " + lname
        self.all_allocations[person][1] = room_name
        pass

    def load_people(self):
        f = open('/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/files/person.txt','r')
        dct = {}
        count = 0
        for line in f:
            item = line.split()
            self.add_person(item[0], item[1], item[2], item[3])
        print self.all_persons
        print self.all_allocations

amity = AmityControls()
amity.load_people()
