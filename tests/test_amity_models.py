''' Importing unittest '''
import unittest
from unittest import TestCase
from models.amity_models import Office, LivingSpace, Fellow, Staff

class AmityModelTest(TestCase):
    """ Class AmityModelTest Creation"""

    def test_office_maximum_number(self):
        '''
        Function for checking Office maximum number
        Returns:
        The return value. True for 6, False otherwise.
        '''
        office = Office()
        self.assertEqual(office.maximum_capacity, 6, msg="Office maximum capacity has not set to 6")

    def test_livingspace_maximum_number(self):
        '''
        Function for checking Living Space maximum number
        Returns:
        The return value. True for 4, False otherwise.
        '''
        livingspace = LivingSpace()
        self.assertEqual(livingspace.maximum_capacity, 4,
                         msg="LivingSpace maximum capacity has not set to 4")

    def test_office_room_type(self):
        '''
        Function for validating Office room_type
        Returns:
        The return value. True for Office, False otherwise.
        '''
        office = Office()
        self.assertEqual(office.room_type, "Office",
                         msg="Office room-type has not been set to Office")

    def test_livingspace_room_type(self):
        '''
        Function for validating Office room_type
        Returns:
        The return value. True for Living Space, False otherwise.
        '''
        livingspace = LivingSpace()
        self.assertEqual(livingspace.room_type, "Living Space",
                         msg="LivingSpace room-type has not been set to Living Space")

    def test_fellow_person_type(self):
        '''
        Function for validating Fellow person_type
        Returns:
        The return value. True for Fellow, False otherwise.
        '''
        fellow = Fellow()
        self.assertEqual(fellow.person_type, "FELLOW",
                         msg="Fellow person-type has not been set to Fellow")

    def test_staff_person_type(self):
        '''
        Function for validating Staff person_type
        Returns:
        The return value. True for Staff, False otherwise.
        '''
        staff = Staff()
        self.assertEqual(staff.person_type, "STAFF",
                         msg="Staff person-type has not been set to Staff")


if __name__ == '__main__':
    unittest.main()
