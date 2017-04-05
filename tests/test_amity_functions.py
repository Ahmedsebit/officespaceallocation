''' Importing unittest '''
import unittest
from unittest import TestCase
import sys
from functions import amity_functions



class AmityControlTest(TestCase):
    ''' Creating AmityControlTest class'''
    def setUp(self):
        self.amity = AmityControls()
        self.person_list = ['Staff', 'Fellow']
        self.room_list = ['Office', 'Living SPace']


    def test_load_state(self):

        '''
        Function to check if application has been loaded with data from the database
        True - if data has been loaded (Anity dictionary has items loaded to it)
        False and fails - if data hasn't been loaded
        '''
        count = len(self.amity.amity)
        self.assertGreater(count, 0, msg='Loading Failed')


    def test_createroom_room_exists(self):

        '''
        Function to check if room exists in all_rooms dictionary
        False & Fails - If room doest exists
        '''
        self.assertTrue('Kinshasa' in self.amity.all_rooms, msg="Room does not exist")


    def test_createroom(self):

        '''
        Function to check for succesfull room creation
        True - If room is created (Length of room increments by 1)
        False & Fails - If room creation fails (Length of room remains the same)
        '''
        currentcount = len(self.amity.all_rooms)
        self.amity.create_room('Kigali', 'Office')
        newcount = len(self.amity.all_rooms)
        self.assertEqual(currentcount + 1, newcount, msg="Room not created")


    def test_create_room_invalid_roomtype(self):

        '''
        Function for checking the created room type
        False and Fails if the room type is not 'Office' of 'Living Space'
        '''
        self.amity.create_room('Adis Ababa', 'Staff')
        self.assertIn(self.amity.all_rooms['Adis Ababa'], self.room_list, msg="Wrong Room Type")


    def test_add_person_person_exist(self):

        '''
        Function for checking if person exists
        False and Fails - If person doesnt exists
        '''
        self.assertTrue('Timothy Ngugi' in self.amity.all_persons, msg="Person does not exists")


    def test_add_person(self):

        '''
        Function for checking succesfull person creation
        True - If person is created (Length of room dcitionary increments by 1)
        False & Fails - If person creation fails (Length of room remains the same)
        '''

        currentcount = len(self.amity.all_persons)
        self.amity.add_person('Ahmed', 'Yusuf', 'Fellow', 'Y')
        newcount = len(self.amity.all_persons)
        self.assertEqual(currentcount + 1, newcount, msg="Person not added")


    def test_add_person_invalid_persontype(self):

        '''
        Function for checking the created room type
        Fails if the person type is not 'Fellow' of 'Staff'
        '''

        self.amity.add_person('Ahmed', 'Yusuf', 'Fello', 'Y')
        self.assertIn(self.amity.all_persons['Ahmed Yusuf'],
                      self.person_list, msg="Wrong Room Type")


    def test_add_person_allocate_room(self):

        '''
        Function for checking succesfull room allocation
        True - If person is succesfully allocated (Length of allocation dictionary increments by 1)
        False & Fails - If allocation fails (Length of allocation dictionary  remains the same)
        '''

        currentspaces = len(self.amity.all_allocations)
        self.amity.add_person('Ahmed', 'Yusuf', 'Fellow', 'Y')
        newspaces = len(self.amity.all_allocations)
        self.assertEqual(currentspaces + 1, newspaces, msg="Room not allocated")

    def test_create_roon_invalid_allocation(self):

        '''
        Function for checking living space allocation to staff
        True - If Staff is not allocated a living spce
        Fails - if Staff is allocated a living space
        '''

        self.amity.add_person('T', 'S', 'Staff', 'Y')
        self.assertNotEqual(self.amity.all_persons['T S'], 'Staff',
                            msg="Cannot allocate staff a room")


    def test_reallocate_office(self):

        '''
        Function for checking for succesfull room relocation
        True - If relocation is succesful (The name of the allocated room changes)
        False and Fails - If relocation fails (The name of the allocated room remains the same)
        '''

        old_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.amity.relocate_office('Ahmed', 'Yusuf', 'Office', 'Adis Ababa')
        new_location = self.amity.all_allocations['Ahmed Yusuf'][1]
        self.assertNotEqual(old_location, new_location, msg="Relocation unsuccesfull")



    def test_load_people(self):

        '''
        Function for checking loading persons from text files
        True - If allocations dictionary length increases by number of lines in the text files
        False and Fails - If dictionary length doesn't increase by number of lines in the text files
        '''

        currentspaces = len(self.amity.all_allocations)
        self.amity.load_people('../person.txt')
        files = open('../person.txt', 'r')
        count = 0
        for line in files:
            count += 1

        newspaces = len(self.amity.all_allocations)
        self.assertGreater(currentspaces + count, newspaces, msg="Loading failed")



if __name__ == '__main__':
    unittest.main()
