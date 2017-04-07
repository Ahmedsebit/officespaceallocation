from functions.amity_functions import AmityControls
from models.amity_models import Amity, Fellow, Staff, Office, LivingSpace

class AmityMain(object):

    def __init__(self):
        pass

    def person(self):
        amitycontrols = AmityControls()
        amitycontrols.relocate_office('Fellow', 'One', 'OFFICE', 'OfficeTwo')
        print (amitycontrols.all_allocations)

amitymain = AmityMain()
amitymain.person()
