# officespaceallocation
DESCRIPTION

The peroject involves a room allocation system for a company that accomodates both staff and fellows, with the difference of the staff only have acces to offices while fellows both offices and living space.

Offices can accommodate a maximum of 6 people while living spaces can accommodate a maximum of 4 people. The allocation of the offices and living spaces are done at random.


The building blocks are:

Python 3.6.0
SQLite DB


Devepment Set-Up

prepare directory for a virtual environment:

  $ mkdir -p ~/officespaceallocation
  $ cd ~/officespaceallocation

Create a directory for the virtual environment virtual environment called off_alloc (you can call it anything you wish):

  $ virtualenv python3.6 -m venv off_alloc

activate the virtual environment.

  $ source off_alloc/bin/activate

check out project code:

  $ git clone https://github.com/Ahmedsebit/officespaceallocation.git

install requirements into virtualenv:

  $ pip install -r officespaceallocation/requirements.txt

Run the application in interactive mode using the following command:

  $ python app.py -i
  
 To use the application
    (Leave blank to loading data from the default database or enter name to create a new db)
    app load_state [<file_name.db>] 
    
    (To create a new office or living space. A user can enter multiple rooms)
    app create_room <room_type> ( office | livingspace ) <room_name>....
    
    (To add a new staff or fellow. The name should not include numbers or special characters)
    app add_person <person_type> ( Staff| Fellow ) <first_name> <last_name> [<want_accommodation>]
    
    (For allocating an office to a staff or fellow who had not been allocated any office)
    app allocate_office <first_name> <last_name>
    
    (For allocating an office to a fellow who had not been allocated any office)
    app allocate_livingspace <first_name> <last_name>
    
    (For loading people from a text file. The file should be a text file and the input should have the correct format)
    app load_people <file_name.txt>
    
    (For printing the people in a the room specified)
    app print_room <room_name>
    
    (For printing all the people who have not been allocated offices)
    app print_unallocations [<file_name.txt>]
    
    (For printing all the user who have not been allocated offices)
    app print_allocations [<file_name.txt>]
    
    (For reallocating a user to a different room. Reallocation only happen if they were allocations was done    before)
    app reallocate_person <first_name> <last_name> <room_name>
    
    (For saving the data from the application to db. Leave blank to use the default db or enter a prefered db)
    app save_state [<file_name.db>]
    
    (For loading the application)
    app (-i | --interactive)
    
    (For loading help)
    app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -o, --output  Save to a txt file
    -h, --help  Show this screen and exit.
