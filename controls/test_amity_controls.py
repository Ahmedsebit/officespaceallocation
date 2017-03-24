import unittest
import sys
sys.path.insert(0, '/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/controls')
from unittest import TestCase
from amity_controls import AmityControls

class AmityControlTest(TestCase):
    def setUp(self):
        self.amity = AmityControls()

    def test_if_room_exists(self):
        self.assertFalse('K' in self.amity.all_rooms, msg="Room already exist")


    def test_create_room(self):
        CurrentCount = len(self.amity.all_rooms)
        self.amity.create_room('Adis Ababa', 'Office')
        NewCount = len(self.amity.all_rooms)
        self.assertEqual(CurrentCount + 1, NewCount, msg="Room not created")

    def test_invalid_roomtype(self):
        self.amity.create_room('Adis Ababa', 'Office')
        self.assertEqual(self.amity.all_rooms['Adis Ababa'], "Office", msg="Invalid Type")

    def test_if_person_exist(self):
        self.assertFalse('A' in self.amity.all_allocations, msg="Person already exists")


    def test_add_person(self):
        CurrentCount = len(self.amity.all_persons)
        self.amity.add_person('Sebit', 'Rajab', 'Fellow', 'Y')
        NewCount = len(self.amity.all_persons)
        self.assertEqual(CurrentCount + 1, NewCount, msg="Person not added")

    def test_allocate_room(self):
        CurrentSpaces = len(self.amity.all_allocations)
        self.amity.add_person('T', 'N','Fellow', 'Y')
        NewSpaces = len(self.amity.all_allocations)
        self.assertEqual(CurrentSpaces + 1, NewSpaces, msg="Room not allocated")

    def test_reallocate_office(self):
        old_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.amity.relocate_office('Ahmed', 'Yusuf','Office', 'Adis Ababa')
        new_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.assertNotEqual(old_location, new_location, msg="Relocation unsuccesfull")

    def test_allocate_staff_living_space(self):
        self.amity.add_person('T', 'S', 'Fellow', 'Y')
        self.assertNotEqual(self.amity.all_persons['T S'], 'Staff', msg="Cannot allocate staff a room")

    def test_invalid_input_person(self):
        #self.amity.add_person("1", "2", 3, 'Y')
        #person = self.amity.all_persons[1]
        #self.assertTrue(TypeError)
        pass

    def test_invalid_input_room(self):
        self.amity.create_room(1, "2")
        room = self.amity.all_rooms[1]
        self.assertFalse(isinstance(room, int), msg="Invalid input")

    def test_load_people(self):
        CurrentCount = len(self.amity.all_allocations)
        f = open('/Users/ahmedyusuf/desktop/CP1AOfficeSpaceAllocation/officespaceallocation/files/person.txt','r')
        count = 0
        for line in f:
            item = line.split()
            self.amity.add_person(item[0], item[1], item[2], item[3])
            count +=1
        NewCount = len(self.amity.all_allocations)
        self.assertEqual(CurrentCount + count, NewCount, msg="None")

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
