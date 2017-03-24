import unittest
from unittest import TestCase
from amity_models import Amity, Room, Office, LivingSpace, Person, Fellow, Staff

class AmityModelTest(TestCase):

    def test_office_inheritance(self):
        issubclass(Office, Room)

    def test_livingspace_inheritance(self):
        issubclass(LivingSpace, Room)

    def test_fellow_inheritance(self):
        issubclass(Fellow, Person)

    def test_staff_inheritance(self):
        self.assertTrue(issubclass(Staff, Room), msg="staff not inheriting")

    def test_office_maximum_number(self):
        office = Office()
        self.assertEqual(office.maximum_capacity, 6)

    def test_livingspace_maximum_number(self):
        livingspace = LivingSpace()
        self.assertEqual(livingspace.maximum_capacity, 4)

    def test_office_room_type(self):
        office = Office()
        self.assertEqual(office.room_type, "Office")

    def test_livingspace_room_type(self):
        livingspace = LivingSpace()
        self.assertEqual(livingspace.room_type, "Living Space")


    def test_fellow_con_type(self):
        fellow = Fellow()
        self.assertEqual(fellow.con_type, "Fellow")

    def test_staff_con_type(self):
        staff = Staff()
        self.assertEqual(staff.con_type, "Staff")


if __name__ == '__main__':
    unittest.main()
