import unittest
from unittest import TestCase
from models import Amity, Room, Office, LivingSpace, Person, Fellow, Staff

class AmityControlTest(TestCase):

    def test_if_room_exists(self):
        AmityControls.create_room('Kigali', 'Office')
        self.assertTrue('Kigali' in Room.all_rooms)
        msg = Amity.create_room('Kigali', 'Office')
        self.assertEqual(msg, "Room already exists")

    def test_create_room(self):
        CurrentCount = len(Room.all_rooms)
        AmityControls.create_room('Kigali', 'Office')
        NewCount = len(Room.all_rooms)
        self.assertEqual(CurrentCount + 1, NewCount)

    def test_if_person_exist(self):
        AmityControls.add_person('Ahmed', 'Fellow', 'Y')
        self.assertTrue('Ahmed' in Person.all_person)
        msg = AmityControls.add_person('Ahmed', 'Fellow', 'Y')
        self.assertEqual(msg, "Person already exists")

    def test_add_person(self):
        CurrentCount = len(Person.all_person)
        msg = AmityControls.add_person('Ahmed', 'Fellow', 'Y')
        NewCount = len(Person.all_person)
        self.assertEqual(CurrentCount + 1, NewCount)

    def test_allocate_room(self):
        CurrentSpaces = len(Person.all_spaces)
        AmityControls.add_person('Ahmed', 'Fellow', 'Y')
        NewSpaces = len(Person.all_spaces)
        self.assertEqual(CurrentCount + 1, NewCount)

    def test_reallocate_office(self):
        old_location = Office['Ahmed']
        AmityControls.relocate_office('Ahmed', 'Office', 'Kigali')
        new_location = Office['Ahmed']
        self.assertIsNotEqual(old_location, new_location)

    def test_allocate_staff_living_space(self):
        AmityControls.add_person('Ahmed', 'Staff', 'Y')
        self.assertNotEqual('Staff')

    def test_invalid input_person(self):
        AmityControls.add_person(1, 2, 3)
        raise TypeError('Invalid Input')

    def test_invalid input_room(self):
        AmityControls.create_room(1, 2)
        raise TypeError('Invalid Input')

    def test_load_people(self):
        pass

    def test_input_is_text(self):
        pass

    def test_space_is_available(self):
        pass

    def test_print_allocations(self):
        pass

    def test_check_for_proper_output(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_check_for_proper_output(self):
        pass

    def test_print_room(self):
        pass



if __name__ == '__main__':
    unittest.main()
