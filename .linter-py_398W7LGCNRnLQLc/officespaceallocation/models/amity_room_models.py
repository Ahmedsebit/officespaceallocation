class Room(object):
    """Base class for creating rooms in amity."""

    def __init__(self, room_name, room_type, capacity, occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.capacity = capacity
        self.occupants = []


class LivingSpace(Room):
    """Creates living spaces and inherits from Room."""

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(
            room_name, room_type="LIVINGSPACE", capacity=4, occupants=[])



class Office(Room):
    """Creates offices and inherits from room."""

    def __init__(self, room_name):
        super(Office, self).__init__(
            room_name, room_type="OFFICE", capacity=6, occupants=[])
