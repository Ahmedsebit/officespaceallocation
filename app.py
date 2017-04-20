"""
Usage:
    app load_state <file_name>
    app create_room <room_type> <room_name>....
    app add_person <person_type> <first_name> <last_name> [<want_accomodation>]
    app print_room <room_name>
    app print_unallocations [-o=filename]
    app print_allocations [-o=filename]
    app reallocate_person <first_name> <last_name> <room_name>
    app save_state
    app (-i | --interactive)
    app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -o, --output  Save to a txt file
    -h, --help  Show this screen and exit.
"""

import cmd
import sys
from docopt import docopt, DocoptExit
from termcolor import cprint, colored
from pyfiglet import Figlet, figlet_format
from functions.amity_functions import AmityControls
from models.amity_room_models import Room, Office, LivingSpace
from models.amity_models import Amity
from models.amity_person_models import Person, Fellow, Staff


def docopt_cmd(func):


    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn



class MyInteractive(cmd.Cmd):
    amity_controls = AmityControls()
    cprint(figlet_format("Amity", font="isometric4"), attrs=['bold'])
    prompt = '(app) '
    file = None
    print(__doc__)


    @docopt_cmd
    def do_create_room(self, args):

        """Usage: create_room <room_type> <room_name>..."""
        room_type = args['<room_type>'].upper()
        for name in args['<room_name>']:
            room_name = args['<room_name>'][args['<room_name>'].index(name)]
            cprint(self.amity_controls.create_room(room_name, room_type))


    @docopt_cmd
    def do_add_person(self, args):

        """Usage: add_person <person_type> <first_name> <last_name> [<want_accomodation>] """
        role = args['<person_type>'].upper()
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        if args['<want_accomodation>'] is None:
            want_accommodation = 'N'
        else:
            want_accommodation = args['want_accommodation']
        cprint(self.amity_controls.add_person(first_name, last_name, role, want_accommodation))



    @docopt_cmd
    def do_reallocate_person(self, args):

        """Usage: reallocate_person <first_name> <last_name> <room_name>"""
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        room_name = args['<room_name>']
        person_name = first_name + " " + last_name
        cprint(self.amity_controls.reallocate_person(first_name, last_name, room_name))



    @docopt_cmd
    def do_print_room(self, arg):

        """Usage: print_room <room_name>"""
        room_name = arg['<room_name>']
        cprint(self.amity_controls.print_room(room_name))

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name>]"""
        file_name = arg['<file_name>']
        cprint(self.amity_controls.print_allocations(file_name))

    @docopt_cmd
    def do_print_unallocations(self, arg):
        """Usage: print_unallocations <file_name>"""
        file_name = arg['<file_name>']
        cprint(self.amity_controls.print_unallocations(file_name))


    @docopt_cmd
    def do_load_state(self, arg):

        """Usage: load_state <file_name>"""
        filename = arg['<file_name>']
        cprint(self.amity_controls.load_state(filename))

    @docopt_cmd
    def do_save_state(self, arg):

        """Usage: save_state <file_name>"""
        filename = arg['<file_name>']
        cprint(self.amity_controls.save_state(filename))

    def do_quit(self, args):

        """Quits out of Interactive Mode."""
        cprint('Good Bye!')
        exit()





opt = docopt(__doc__, sys.argv[1:])





if opt['--interactive']:
    MyInteractive().cmdloop()



print(opt)
