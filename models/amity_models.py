""" Class Amity Creation"""

class Amity(object):
    def __init__(self):
        self.all_allocations = {"Fellow One":["OfficeOne", "LivingSpaceOne"],
                                "Fellow Two":["OfficeTwo"], "Staff One":["OfficeOne"]}

class Room(object):
    """ Class Amity Creation"""
    def __init__(self, room_type, maximum_capacity):
        pass

class Office(object):
    """ Class Amity Creation"""
    def __init__(self):
        self.maximum_capacity = 6
        self.room_type = "Office"
        self.all_Offices = {'OfficeOne':2, 'OfficeTwo':1}

class LivingSpace(object):
    """ Class Amity Creation"""
    def __init__(self):
        self.maximum_capacity = 4
        self.room_type = "Living Space"
        self.all_Livingspaces = {'LivingSpaceOne':1, 'LivingSpaceTwo':0}

class Person(object):
    """ Class Amity Creation"""
    def __init__(self, person_type):
        pass

class Fellow(object):
    """ Class Amity Creation"""
    def __init__(self):
        self.person_type = "FELLOW"
        self.all_Fellows = ['Fellow One', 'Fellow Two']

class Staff(object):
    """ Class Amity Creation"""
    def __init__(self):
        self.person_type = "STAFF"
        self.all_Staff = ['Staff One']
