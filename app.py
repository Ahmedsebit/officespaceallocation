from functions.amity_functions import AmityControls
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_models import Amity
from models.amity_person_models import Person, Fellow, Staff

class AmityMain(object):

    def __init__(self):
        pass

    def person(self):
        # amity_functions = AmityControls()
        # x = Office('Test Office')
        # y = LivingSpace('Test Living Spaces')
        # a = Fellow('Ahmed')
        # b = Staff('Yusuf')
        # a.accom = 'Y'
        # c = Fellow('Sebit')
        # d = Staff('Rajab')
        # g = Amity()
        #
        #
        # x.occupants.append(a)
        # y.occupants.append(b)
        # x.occupants.append(c)
        # y.occupants.append(d)
        #
        # g.all_rooms.append(x)
        # g.all_rooms.append(y)
        #
        # print (x.room_name, x.room_type, len(x.occupants))
        # print (y.room_name, y.room_type, len(y.occupants))
        # print (a.person_name, a.person_type, a.accom)
        # print (len(g.all_rooms))
        #
        # h = [x.room_name for x in g.all_rooms]
        #
        # if 'Test Offices' in h:
        #     print ('Exists')
        # else:
        #     print ('Doesnt exists')

        amity_controls = AmityControls()
        amity = Amity()
        amity_controls.create_room('Amity', 'Office')
        amity_controls.create_room('AmityLiving', 'Living Space')
        amity_controls.create_room('AmityOff', 'Office')
        amity_controls.create_room('AmityLiv', 'Living Space')
        amity_controls.add_person('Ahmed', 'Yusuf', 'Fellow', 'Y')
        offices = [x for x in amity_controls.rooms if x.room_type == 'OFFICE']
        livingspaces = [x for x in amity_controls.rooms if x.room_type == "LIVING SPACE"]
        print (amity_controls.persons)
        print (amity_controls.rooms)
        print (offices)
        print (livingspaces)
amitymain = AmityMain()
amitymain.person()
