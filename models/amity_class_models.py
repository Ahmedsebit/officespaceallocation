""" Class Amity Creation"""

class Amity(object):
    def __init__(self):
        self.all_allocations = {"Fellow One":["OfficeOne", "LivingSpaceOne"],
                                "Fellow Two":["OfficeTwo"], "Staff One":["OfficeOne"]}

class Room(object):
    """ Class Amity Creation"""
    def __init__(self, room_name, room_type, maximum_capacity, occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.maximum_capacity = maximum_capacity
        self.occupants = []

    def isfull(self):
        if len(self.occupants) < self.maximum_capacity:
            return True
        else:
            return False


class Office(Room):
    """ Class Amity Creation"""
    def __init__(self, room_name):
        super(Office, self).__init__(
            room_name, maximum_capacity=6, room_type="OFFICE", occupants=[])

class LivingSpace(Room):
    """ Class Amity Creation"""
    def __init__(self, room_name):
        super(Office, self).__init__(
            room_name, maximum_capacity=4, room_type="LIVING SPACE", occupants=[])

class Person(object):
    """ Class Amity Creation"""
    def __init__(self, person_name, person_type, accomodation):
        self.person_name = person_name
        self.person_type = person_type
        self.accomodation = accomodation

class Fellow(object):
    """ Class Amity Creation"""
    def __init__(self):
        super(Fellow, self).__init__(
            person_name, person_type="FELLOW", accomodation="N")

class Staff(object):
    """ Class Amity Creation"""
    def __init__(self):
        super(Staff, self).__init__(
            person_name, person_type="STAFF", accomodation="N")
