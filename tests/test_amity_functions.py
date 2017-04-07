''' Importing unittest '''
import unittest
from unittest import TestCase
from functions.amity_functions import AmityControls
from models.amity_models import Amity, Fellow, Staff


class AmityControlTest(TestCase):
    ''' Creating AmityControlTest class'''
    def setUp(self):
        self.amity = AmityControls()
        self.amity_class = Amity()


    def test_load_state(self):
        '''
        Function to check if application has been loaded with data from the database
        True - if data has been loaded (Anity dictionary has items loaded to it)
        False and fails - if data hasn't been loaded
        '''
        self.assertEqual(self.amity.load_state(), 'System Loaded', msg='Loading Failed')


    def test_createroom(self):
        '''
        Function to check for succesfull room creation
        True - If room is created (Length of room increments by 1)
        False & Fails - If room creation fails (Length of room remains the same)
        '''
        self.assertEqual(self.amity.create_room('London', 'OFFICE'),
                         'Room succefully created', msg="Room not created")


    def test_createroom_room_exists(self):
        '''
        Function to check if room exists in rooms list
        False & Fails - If room doest exists
        '''
        self.amity.create_room('London', 'OFFICE')
        self.assertEqual(self.amity.create_room('London', 'OFFICE'),
                         'Room already exists', msg="Room already exist")


    def test_create_room_invalid_roomtype(self):
        '''
        Function for checking the created room type
        False and Fails if the room type is not 'Office' of 'Living Space'
        '''
        self.assertEqual(self.amity.create_room('Adis Ababa', 'Staff'),
                         'Invalid room type, Should be OFFICE or LIVING SPACE')


    def test_add_person_person_exist(self):
        '''
        Function for checking if person exists
        False and Fails - If person doesnt exists
        '''
        self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y')
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y'),
                         'The person already exists')


    def test_add_person(self):
        '''
        Function for checking succesfull person creation
        True - If person is created (Length of room dcitionary increments by 1)
        False & Fails - If person creation fails (Length of room remains the same)
        '''
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y'),
                         'Person Succesfully Added', msg="Person already exists")


    def test_add_person_invalid_persontype(self):
        '''
        Function for checking for person type
        Fails if the person type is not 'Fellow' of 'Staff'
        '''
        self.amity.add_person('Timothy', 'Ngugi', 'FELLO', 'Y')
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLO', 'Y'),
                         'Wrong person type, should be FELLOW or STAFF', msg="Wrong Person Type")


    def test_allocate_room_fellowall(self):
        '''
        Function for checking succesfull all rooms allocation
        True - If person is succesfully allocated (Length of allocation dictionary increments by 1)
        False & Fails - If allocation fails (Length of allocation dictionary  remains the same)
        '''
        self.assertEqual(self.amity.allocate_room('Ahmed Yusuf', 'FELLOW', 'Y'),
                         'Office and Living Space succesfully allocated')


    def test_allocate_room_fellowoffice(self):
        '''
        Function for checking succesfull office allocation
        True - If person is succesfully allocated (Length of allocation dictionary increments by 1)
        False & Fails - If allocation fails (Length of allocation dictionary  remains the same)
        '''
        self.assertEqual(self.amity.allocate_room('Ahmed Yusuf', 'FELLOW', 'N'),
                         'Office succesfully allocated')


    def test_allocate_room_staff(self):
        '''
        Function for checking allocation to staff
        True - If Staff is not allocated a living spce
        Fails - if Staff is allocated a living space
        '''
        self.assertEqual(self.amity.allocate_room('T S', 'STAFF', 'N'),
                         'STAFF succesfully allocated')


    def test_allocate_room_stafflivingspace(self):
        '''
        Function for checking living space allocation to staff
        True - If Staff is not allocated a living spce
        Fails - if Staff is allocated a living space
        '''
        self.assertEqual(self.amity.allocate_room('T S', 'STAFF', 'Y'),
                         'Office Succesfully allocated. Cannot allocate staff a living space')


    def test_reallocate_office(self):
        '''
        Function for checking for succesfull room relocation
        True - If relocation is succesful (The name of the allocated room changes)
        False and Fails - If relocation fails (The name of the allocated room remains the same)
        '''
        self.amity.allocate_room('Fellow Three', 'OFFICE', 'OfficeTwo')
        self.assertEqual(self.amity.relocate_office('Fellow Three', 'OFFICE', 'OfficeThree'),
                         'Relocation succesful')


    def test_load_people_succefull(self):
        '''
        Function for checking loading persons from text files
        True - If allocations dictionary length increases by number of lines in the text files
        False and Fails - If dictionary length doesn't increase by number of lines in the text files
        '''
        self.assertEqual(self.amity.load_people('person.txt'),
                         'Loading succesful', msg="Loading failed")

    def test_load_people_invalidfile(self):
        '''
        Function for checking loading persons from text files
        True - If allocations dictionary length increases by number of lines in the text files
        False and Fails - If dictionary length doesn't increase by number of lines in the text files
        '''
        self.assertEqual(self.amity.load_people('person_invalid.txt'),
                         'Loading Failed, Invalid failed', msg="Loading failed")

    def test_load_people_emptyfile(self):
        '''
        Function for checking loading persons from text files
        True - If allocations dictionary length increases by number of lines in the text files
        False and Fails - If dictionary length doesn't increase by number of lines in the text files
        '''
        self.assertEqual(self.amity.load_people('person_empty.txt'),
                         'Loading Failed, empty file')

    def test_load_people_nofile(self):
        '''
        Function for checking loading persons from text files
        True - If allocations dictionary length increases by number of lines in the text files
        False and Fails - If dictionary length doesn't increase by number of lines in the text files
        '''
        self.assertRaises(self.amity.load_people('person_notexisting.txt'), OSError)



if __name__ == '__main__':
    unittest.main()
