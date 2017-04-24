import re

class Testing(object):

    def words(self, x):
        if re.match("^[a-zA-Z]*$", x):
            print ("Valid")
        else:
            print ("Invalid")


testing = Testing()
testing.words('Ahmed_')
