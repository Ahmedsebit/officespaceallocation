''' Importing unittest '''
import unittest
from unittest import TestCase
from functions.amity_functions import AmityControls
from models.amity_models import Amity
from models.amity_person_models import Staff, Fellow
from models.amity_room_models import Office, LivingSpace


class AmityControlTest(TestCase):
    ''' Creating AmityControlTest class'''
    def setUp(self):
        self.amity = AmityControls()
        self.amity_class = Amity()


    def test_load_state(self):
        '''
        Function to check if application has been loaded with data from the database
        '''
        self.assertEqual(self.amity.load_state('amity.db'), 'Loading state succesfull')

    def test_invalidfile_load_state(self):
        '''
        Function to check if application has been loaded with invalid data file
        '''
        self.assertEqual(self.amity.load_state('invalid_file'), 'Loading state failed. File type error')

    def test_invalidfiletype_load_state(self):
        '''
        Function to check if application has been loaded with invalid data type faile
        '''
        self.assertEqual(self.amity.load_state('invalid_file.txt'), 'Loading state failed. Wrong file type')


    def test_create_room_office(self):
        '''
        Function to check for succesful office creation
        '''
        self.assertEqual(self.amity.create_room('London', 'OFFICE'),
                         'LONDON office succesfully created')

    def test_create_room_livingspace(self):
        '''
        Function to check for succesful living space creation
        '''
        self.assertEqual(self.amity.create_room('PHP', 'LIVINGSPACE'),
                         'PHP living space succesfully created')


    def test_create_room_existing(self):
        '''
        Function to check if room exists in rooms list
        '''
        self.amity.create_room('London', 'OFFICE')
        self.assertEqual(self.amity.create_room('London', 'OFFICE'),
                         'Room exists')


    def test_create_room_invalid_roomtype(self):
        '''
        Function for checking the wrong room type
        '''
        self.assertEqual(self.amity.create_room('AdisAbaba', 'Staff'),
                         'Invalid room type')


    def test_add_person_person_exist(self):
        '''
        Function for checking if person already exists
        '''
        self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y')
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y'),
                         'The person already exists')


    def test_add_person_fellow(self):
        '''
        Function for checking succesful person creation
        '''
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLOW', 'Y'),
                         'Timothy Ngugi succesfully added')


    def test_add_person_invalid_persontype(self):
        '''
        Function for checking for wrong person type
        '''
        self.amity.add_person('Timothy', 'Ngugi', 'FELLO', 'Y')
        self.assertEqual(self.amity.add_person('Timothy', 'Ngugi', 'FELLO', 'Y'),
                         'Invalid role. Person not created')


    def test_fellow_room_allocation(self):
        '''
        Function for checking succesful al rooms allocation
        '''
        self.amity.create_room('London', 'OFFICE')
        self.amity.create_room('SWIFT', 'LIVINGSPACE')
        self.amity.add_person('Ahmed Yusuf', 'FELLOW', 'Y')
        self.assertEqual(self.amity.add_person('Ahmed', 'Yusuf', 'FELLOW', 'Y'),
                         'Ahmed Yusuf succesfully added')


    def test_add_person_staff(self):
        '''
        Function for staff addition
        '''
        self.assertEqual(self.amity.add_person('T', 'S', 'STAFF', 'N'),
                         'T S succesfully added')


    def test_staff_livingspace_allocation(self):
        '''
        Function for checking living space allocation to staff
        '''
        self.amity.create_room('London', 'OFFICE')
        self.amity.create_room('SWIFT', 'LIVINGSPACE')
        self.assertEqual(self.amity.add_person('T', 'S', 'STAFF', 'Y'),
                         'T S succesfully Added to Office. Cannot allocate staff a livingspace')


    def test_reallocate_office(self):
        '''
        Function for checking for succesful room relocation
        '''
        self.amity.create_room('London', 'OFFICE')
        self.amity.add_person('A', 'Y', 'FELLOW')
        self.amity.create_room('Kinshasa', 'OFFICE')
        self.assertEqual(self.amity.reallocate_person('A', 'Y', 'KINSHASA'),
                         'A Y  was reallocated succesfully from LONDON to KINSHASA')

    def test_reallocate_office_exists(self):
        '''
        Function for checking for reallocation to same room
        '''
        self.amity.create_room('Kinshasa', 'OFFICE')
        self.amity.add_person('A', 'Y', 'FELLOW')
        self.assertEqual(self.amity.reallocate_person('A', 'Y', 'KINSHASA'),
                         'The person already exists in the room')


    def test_load_people_succefull(self):
        '''
        Function for checking loading persons from text files
        '''
        self.assertEqual(self.amity.load_people('person.txt'),
                         'People loaded succesfully')

    def test_load_people_invalidfile(self):
        '''
        Function for checking loading persons from invalid text file
        '''
        self.assertEqual(self.amity.load_people('person_invalid.txt'),
                         'Invalid file')


    def test_load_people_nofile(self):
        '''
        Function for checking loading persons from non existing text files
        '''
        self.assertEqual(self.amity.load_people('person_notexisting.txt'),
                         'Invalid file')


    def test_save_state(self):
        '''
        Function to check if application has been loaded with data from the database
        '''
        self.assertEqual(self.amity.save_state('amity.db'), 'State saved')

    def test_print_unallocations(self):
        '''
        Function to check if application has been loaded with invalid data type
        '''
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_unallocations('amity.txt'), 'Unallocated persons printed to :amity.txt')

    def test_print_unallocations_invalidfilename(self):
        '''
        Function to check if application has been loaded with in valid data type
        '''
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_unallocations('amity'), 'Invalid file')

    def test_print_unallocations_invalidfiletype(self):
        '''
        Function to check if unallocated people have been printed to an invalid data type
        '''
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_unallocations('amity.db'), 'Invalid file type')

    def test_print_allocations(self):
        '''
        Function to check if unallocated people have been printed to an valid data file
        '''
        self.amity.create_room('LONDON', 'OFFICE')
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_allocations('amity.txt'), 'Allocations printed to :amity.txt')

    def test_print_allocations_invalidfilename(self):
        '''
        self.amity.create_room('LONDON', 'OFFICE')
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        Function to check if unallocated people have been printed to an invalid data file
        '''

        self.amity.create_room('LONDON', 'OFFICE')
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_allocations('amity'), 'Invalid file')

    def test_print_allocations_invalidfiletype(self):
        '''
        Function to check if allocated people have been printed to an invalid data type
        '''

        self.amity.create_room('LONDON', 'OFFICE')
        self.amity.add_person('AHmed', 'Yusuf', 'Fellow')
        self.assertEqual(self.amity.print_allocations('amity.db'), 'Invalid file type')

    def test_print_room(self):
        '''
        Function to check if printing a room and the occupants was succesful
        '''
        self.amity.create_room('London', 'OFFICE')
        self.amity.add_person('A', 'Y', 'FELLOW')
        self.assertEqual(self.amity.print_room('LONDON'), 'LONDON'+"\n"
                         +"['A Y']")
    def test_empty_print_room(self):
        '''
        Function to check for printing a room with no occupants
        '''
        self.amity.create_room('London', 'OFFICE')
        self.assertEqual(self.amity.print_room('LONDON'), 'LONDON'+"\n"+"[]")

    def test_print_room_notexisting(self):
        '''
        Function to check for printing ocupants for a non-existing room
        '''
        self.assertEqual(self.amity.print_room('LONDON'), 'Room does not exist')

    def test_invalidfile_save_state(self):
        '''
        Function to check if application has been saved to an invaid file
        '''
        self.assertEqual(self.amity.save_state('invalid_file'), 'Saving state failed. File type error')

    def test_invalidfiletype_save_state(self):
        '''
        Function to check if application has been saved to an invalid file type
        '''
        self.assertEqual(self.amity.save_state('invalid_file.txt'), 'Saving state failed. Wrong file type')

if __name__ == '__main__':
    unittest.main()
