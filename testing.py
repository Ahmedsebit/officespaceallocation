from functions.amity_functions import AmityControls
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_models import Amity
from models.amity_person_models import Person, Fellow, Staff
from database.database_functions import AmityDatabase
from database.database_models import Initialize

class Testing(object):

    def save_database(self):
        amity = AmityControls()

        amity.save_state('invalid_file2')



amity_testing = Testing()
amity_testing.save_database()
