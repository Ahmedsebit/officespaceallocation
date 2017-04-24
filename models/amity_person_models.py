class Person(object):
    """Base class for creating person in amity."""

    def __init__(self, person_name, person_type, want_accommodation):
        self.person_name = person_name
        self.person_type = person_type
        self.want_accommodation = want_accommodation


class Fellow(Person):
    """Creates Fellow and inherits from Person"""

    def __init__(self, person_name):
        super(Fellow, self).__init__(
            person_name, person_type="FELLOW", want_accommodation='N')



class Staff(Person):
    """Creates Staff and inherits from Person."""

    def __init__(self, person_name):
        super(Staff, self).__init__(
            person_name, person_type="STAFF", want_accommodation='N')
