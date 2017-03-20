class Amity(object):
    def __init__(self):
        pass

class Room(object):
    def __init__(self, room_type, maximum_number):
        pass

class Office(Room):
    def __init__(self):
        self.maximum_capacity = 6
        self.room_type = "Office"
        pass

class LivingSpace(Room):
    def __init__(self):
        self.maximum_capacity = 4
        self.room_type = "Living Space"
        pass

class Person(object):
    def __init__(self, con_type):
        pass

class Fellow(Person):
    def __init__(self):
        self.con_type = "Fellow"
        pass

class Staff(Person):
    def __init__(self):
        self.con_type = "Staff"
        pass
