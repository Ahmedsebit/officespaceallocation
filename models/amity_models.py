
import os
import sys


class Amity(object):
    def __init__(self):
        pass

class Room(object):
    def __init__(self, room_type, maximum_capacity):
        pass

class Office(object):
    def __init__(self):
        self.maximum_capacity = 0
        self.room_type = ""
        pass

class LivingSpace(object):
    def __init__(self):
        self.maximum_capacity = 0
        self.room_type = ""
        pass

class Person(object):
    def __init__(self, con_type):
        pass

class Fellow(object):
    def __init__(self):
        self.con_type = ""
        pass

class Staff(object):
    def __init__(self):
        self.con_type = ""
        pass
