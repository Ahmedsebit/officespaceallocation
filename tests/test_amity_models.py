import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
from unittest import TestCase
from amity_app.models.amity_models import Amity, Room, Office, LivingSpace, Person, Fellow, Staff

class AmityModelTest(TestCase):

    def test_office_inheritance(self):
        '''Testing if Office is a subclass of Room'''
        self.assertTrue(issubclass(Office, Room), msg="Office not a subclass of Room")

    def test_livingspace_inheritance(self):
        '''Testing if LivingSpace is a subclass of Room'''
        self.assertTrue(issubclass(LivingSpace, Room), msg="LivingSpace not a subclass of Room")

    def test_fellow_inheritance(self):
        '''Testing if Fellow is a subclass of Person'''
        self.assertTrue(issubclass(Fellow, Person), msg="Felow not a subclass of Person")

    def test_staff_inheritance(self):
        '''Testing if Staff is a subclass of Person'''
        self.assertTrue(issubclass(Staff, Room), msg="Staff not a subclass of Person")

    def test_office_maximum_number(self):
        '''Testing for Office maximum number'''
        office = Office()
        self.assertEqual(office.maximum_capacity, 6, msg="Office maximum capacity has not set to 6")

    def test_livingspace_maximum_number(self):
        '''Testing for LivingSpace maximum number'''
        livingspace = LivingSpace()
        self.assertEqual(livingspace.maximum_capacity, 4, msg="LivingSpace maximum capacity has not set to 4")

    def test_office_room_type(self):
        '''Testing for Office room-type'''
        office = Office()
        self.assertEqual(office.room_type, "Office", msg="Office room-type has not been set to Office")

    def test_livingspace_room_type(self):
        '''Testing for LivingSpace room-type'''
        livingspace = LivingSpace()
        self.assertEqual(livingspace.room_type, "Living Space", msg="LivingSpace room-type has not been set to Living Space")

    def test_fellow_con_type(self):
        '''Testing for Fellow person-type'''
        fellow = Fellow()
        self.assertEqual(fellow.con_type, "Fellow", msg="Fellow person-type has not been set to Fellow")

    def test_staff_con_type(self):
        '''Testing for Staff person-type'''
        staff = Staff()
        self.assertEqual(staff.con_type, "Staff", msg="Staff person-type has not been set to Staff")


if __name__ == '__main__':
    unittest.main()
