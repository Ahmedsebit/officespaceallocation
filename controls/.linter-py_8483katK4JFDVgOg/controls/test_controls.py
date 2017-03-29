import unittest
import sys
sys.path.insert(0, '/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/controls')
from unittest import TestCase
from amity_controls import AmityControls

class AmityControlTest(TestCase):
    def setUp(self):
        self.amity = AmityControls()

    def test_if_room_exists(self):
        '''Test for searching if room exists'''
        self.assertTrue('K' in self.amity.all_rooms, msg="Room does not exist")


    def test_create_room(self):
        '''Test for succesfull room created'''
        CurrentCount = len(self.amity.all_rooms)
        self.amity.create_room('Kigali', 'Office')
        NewCount = len(self.amity.all_rooms)
        self.assertEqual(CurrentCount + 1, NewCount, msg="Room not created")

    def test_invalid_roomtype(self):
        '''Test for checking the created room type'''
        self.amity.create_room('Adis Ababa', 'Off')
        self.assertEqual(self.amity.all_rooms['Adis Ababa'], "Office", msg="Invalid Room Type")

    def test_if_person_exist(self):
        '''Test for searching if person exists'''
        self.assertTrue('A' in self.amity.all_allocations, msg="Person doe not exists")


    def test_add_person(self):
        '''Test for succesfull person created'''
        CurrentCount = len(self.amity.all_persons)
        self.amity.add_person('Ahmed', 'Yusuf', 'Fellow', 'Y')
        NewCount = len(self.amity.all_persons)
        self.assertEqual(CurrentCount + 1, NewCount, msg="Person not added")

    def test_allocate_room(self):
        '''Test for succesfull room allocation'''
        CurrentSpaces = len(self.amity.all_allocations)
        self.amity.add_person('Ahmed', 'Yusuf','Fellow', 'Y')
        NewSpaces = len(self.amity.all_allocations)
        self.assertEqual(CurrentSpaces + 1, NewSpaces, msg="Room not allocated")

    def test_reallocate_office(self):
        '''Test for succesfull room relocation'''
        old_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.amity.relocate_office('Ahmed', 'Yusuf','Office', 'Adis Ababa')
        new_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.assertNotEqual(old_location, new_location, msg="Relocation unsuccesfull")

    def test_allocate_staff_living_space(self):
        '''Test for wrong living space allocation'''
        self.amity.add_person('T', 'S', 'Staff', 'Y')
        self.assertNotEqual(self.amity.all_persons['T S'], 'Staff', msg="Cannot allocate staff a room")

    # def test_invalid_input_person(self):
    #     #self.amity.add_person("1", "2", 3, 'Y')
    #     #person = self.amity.all_persons[1]
    #     #self.assertTrue(TypeError)
    #     pass

    def test_invalid_input_room(self):
        '''Test for wrong room input'''
        self.amity.create_room(1, 2)
        room = self.amity.all_rooms[1]
        self.assertFalse(isinstance(room, int), msg="Invalid input")

    def test_load_people(self):
        '''Test for succesfull room created'''
        CurrentSpaces = len(self.amity.all_allocations)
        self.amity.load_people('/Users/ahmedyusuf/desktop/person.txt')
        NewSpaces = len(self.amity.all_allocations)
        self.assertEqual(CurrentSpaces + 1, NewSpaces, msg="Loading failed")

    # def test_print_unallocated(self):
    #     pass
    #
    # def test_check_for_proper_output(self):
    #     pass
    #
    # def test_print_room(self):
    #     pass



if __name__ == '__main__':
    unittest.main()
