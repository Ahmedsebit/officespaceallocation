import sys
import random
sys.path.insert(0, '/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/controls')

class AmityControls():
    def __init__(self):
        self.all_persons = {"Ahmed Yusuf":"Fellow", "Yusuf":"Staff"}
        self.all_rooms = {"Kigali":"Office","Krypton":"Living Space","Kampala":"Office","Gotham":"Living Space"}
        self.all_allocations = {"Ahmed Yusuf":["Kigali","Krypton"],"Yusuf Sebit":["Kampala"],"T MK":["Kampala","Gotham"]}
        self.selected_room = {}

    def create_room(self, room_name, room_type):
        self.all_rooms.update({room_name:room_type})
        pass

    def add_person(self, fname, lname, role, accom):
        name = fname+ " "+lname
        self.all_persons.update({name:role})
        offices = {k: v for k, v in self.all_rooms.items() if v == "Office"}
        livingspaces = {k: v for k, v in self.all_rooms.items() if v == "Living Space"}
        office = random.choice(list(offices))
        livingspace = random.choice(list(livingspaces))
        self.all_allocations.update({name:[office,livingspace]})

    def relocate_office(self, fname, lname ,reloc_type, room_name ):
        person = fname + " " + lname
        #self.all_allocations[person][1] = room_name

    def load_people(self, text_input):
        f = open(text_input,'r')
        dct = {}
        count = 0
        for line in f:
            item = line.split()
            #self.add_person(item[0], item[1], item[2], item[3])
            return self.all_allocations

    def print_room(self, name):
        selected_room = {k: v for k, v in self.all_allocations.items() if v[0] == name}
        return selected_room



# amity = AmityControls()
# amity.load_people('/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/files/person.txt')
