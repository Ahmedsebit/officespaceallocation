class Person(object):
    """Base class for creating rooms in amity."""

    def __init__(self, person_name, person_type, accomodation):
        self.person_name = person_name
        self.person_type = person_type
        self.accomodation = accomodation


class Fellow(Person):
    """Creates living spaces and inherits from Room."""

    def __init__(self, person_name):
        super(Fellow, self).__init__(
            person_name, person_type="Fellow", accomodation='N')



class Staff(Person):
    """Creates offices and inherits from room."""

    def __init__(self, person_name):
        super(Staff, self).__init__(
            person_name, person_type="Staff", accomodation='N')
