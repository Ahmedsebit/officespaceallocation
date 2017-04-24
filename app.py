"""
Usage:
    app load_state [<file_name.db>]
    app create_room <room_type> ( office | livingspace ) <room_name>....
    app add_person <person_type> ( Staff| Fellow ) <first_name> <last_name> [<want_accommodation>]
    app allocate_office <first_name> <last_name>
    app allocate_livingspace <first_name> <last_name>
    app load_people <file_name.txt>
    app print_room <room_name>
    app print_unallocations [<file_name.txt>]
    app print_allocations [<file_name.txt>]
    app reallocate_person <first_name> <last_name> <room_name>
    app save_state [<file_name.db>]
    app (-i | --interactive)
    app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -o, --output  Save to a txt file
    -h, --help  Show this screen and exit.
"""

import cmd
import sys
import re
from docopt import docopt, DocoptExit
from termcolor import cprint, colored
from pyfiglet import Figlet, figlet_format
from functions.amity_functions import AmityControls


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
    cprint(figlet_format("Amity", font="isometric4"), "green", attrs=['bold'])
    prompt = '(app) '
    file = None
    print(__doc__)


    @docopt_cmd
    def do_create_room(self, args):

        """Usage: create_room <room_type> <room_name>..."""
        room_type = args['<room_type>'].upper()
        for name in args['<room_name>']:
            room_name = args['<room_name>'][args['<room_name>'].index(name)]
            cprint(self.amity_controls.create_room(room_name, room_type), "green")


    @docopt_cmd
    def do_add_person(self, args):

        """Usage: add_person <person_type> <first_name> <last_name> [<want_accommodation>]"""
        role = args['<person_type>'].upper()
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        if re.match("^[a-zA-Z]*$", first_name) and re.match("^[a-zA-Z]*$", last_name):
            if args['<want_accommodation>'] is None:
                accommodation = 'N'
            else:
                accommodation = args['<want_accommodation>']
            accommodation = accommodation.upper()

            cprint(self.amity_controls.add_person(first_name, last_name, role, want_accommodation=accommodation),"green")
        else:
            print ("Name has numbers or special characters")




    @docopt_cmd
    def do_allocate_office(self, args):

        """Usage: allocate_office <first_name> <last_name> """
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        person_name = first_name + " " + last_name
        cprint(self.amity_controls.new_allocate_office(person_name), "green")


    @docopt_cmd
    def do_allocate_livingspace(self, args):

        """Usage: allocate_livingspace <first_name> <last_name> """
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        person_name = first_name + " " + last_name
        cprint(self.amity_controls.new_allocate_livingspace(person_name), "green")


    @docopt_cmd
    def do_reallocate_person(self, args):

        """Usage: reallocate_person <first_name> <last_name> <room_name>"""
        first_name = args['<first_name>'].upper()
        last_name = args['<last_name>'].upper()
        room_name = args['<room_name>']
        person_name = first_name + " " + last_name
        cprint(self.amity_controls.reallocate_person(first_name, last_name, room_name), "green")


    @docopt_cmd
    def do_load_people(self, args):

        """Usage: load_people <file_name.txt> """
        file_name = args['<file_name.txt>']
        cprint(self.amity_controls.load_people(file_name), "green")



    @docopt_cmd
    def do_print_room(self, arg):

        """Usage: print_room <room_name>"""
        room_name = arg['<room_name>']
        room_name = room_name.upper()
        cprint(self.amity_controls.print_room(room_name), "green")

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name.txt>]"""
        if not arg['<file_name.txt>']:
            self.amity_controls.list_allocations()
        else:
            file_name = arg['<file_name.txt>']
            cprint(self.amity_controls.print_allocations(file_name), "green")


    @docopt_cmd
    def do_print_unallocations(self, arg):
        """Usage: print_unallocations [<file_name.txt>]"""
        if not arg['<file_name.txt>']:
            self.amity_controls.list_unallocations()
        else:
            file_name = arg['<file_name.txt>']
            cprint(self.amity_controls.print_unallocations(file_name), "green")


    @docopt_cmd
    def do_load_state(self, arg):

        """Usage: load_state [<file_name.db>]"""
        if not arg['<file_name.db>']:
            filename = 'amity.db'
        else:
            filename = arg['<file_name>']
        cprint(self.amity_controls.load_state(filename), "green")

    @docopt_cmd
    def do_save_state(self, arg):

        """Usage: save_state [<file_name.db>]"""
        if not arg['<file_name.db>']:
            filename = 'amity.db'
        else:
            filename = arg['<file_name.db>']

        cprint(self.amity_controls.save_state(filename), "green")

    def do_quit(self, args):

        """Quits out of Interactive Mode."""
        cprint('Good Bye!', "red")
        exit()





opt = docopt(__doc__, sys.argv[1:])





if opt['--interactive']:
    MyInteractive().cmdloop()



print(opt)
