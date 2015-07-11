__author__ = 'David'
'''



Oliver i edited the class so now it is a easy as pi to have a gui interface

Here are all the calls

changeentry(<window>, <row>, <column>,





*Example program'''

from gui import Gui

win = Gui() #start gui class

def location():
    print "location press"
    Gui.cleargrid(win)  # example how to clear grid

def name():
    print "name press"


def year():
    print "year press"
    Gui.deleteentry(win, 0, 0)

def date():
    print "date press"

def TESTBUTTON():
    print "Test button pressed"

Gui.setdefault(win)  # insert default grid values, such as name, time, year, etc..

Gui.control(win, location, name, year, date)  # Set button controls for sorting (Location, Name, Year, Etc...)


samplearray = ["David Smerkous", "1", "7/11/15", "LS22", "78", ""]

Gui.setrow(win, samplearray, 1)  # fill a whole row 1


secondsample = ["Oliver Warne", "2", "7/13/15", "Collab space", "120", ""]

Gui.setrow(win, secondsample, 5)


columnsample = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

Gui.setcolumn(win, columnsample, 6, Gui.Label, 1)  # Fill a whole column each array num is a location on the column

Gui.changeentry(win, 2, 2, "Edit indv. item", Gui.Label)  # edit individual items

Gui.changeentry(win, 4, 3, "test button", Gui.Button, True, TESTBUTTON)  # Test button on the grid

Gui.start()

'''
* Remember every change call needs to have the gui(root) with it
*
* Now after reading through this code try running it and see how they work with each other
'''