__author__ = 'David/Oliver'
'''
Oliver i edited the class so now it is a easy as pi to have a gui interface
'''


from gui import Gui


'''
VVVVV create a new window in the gui class
'''


win = Gui() #start gui class


'''
VVVVVV button callbacks from the gui panel, so add sorting/sql control here
'''


def location():
    print "location press"
    Gui.cleargrid(win)  # example how to clear grid


def name():
    print "name press"
    Gui.clearrow(win, 1)  # delete a whole row
    Gui.clearcolumn(win, 6)  # delete a whole column


def year():
    print "year press"
    Gui.deleteentry(win, 0, 0)


def date():
    print "date press"
    print "There are " + str(Gui.getcolumns(win)) + " columns"
    print "And there are " + str(Gui.getrows(win)) + " rows"


def TESTBUTTON():
    print "Test button pressed"
    Gui.settitle(win, "Test Button Pressed")


'''
^^^^^ END OF BUTTON CALLBACKS ^^^^^






VVVVVVV set default window/grid system VVVV
'''


Gui.setdefault(win)  # insert default grid values, such as name, time, year, etc..


'''
VVVVV set the control buttons with the callbacks(Look above to see the callbacks VVVVV
'''


Gui.control(win, location, name, year, date)  # Set button controls for sorting (Location, Name, Year, Etc...)


'''
VVVVV add an image to the grid(<window>, <row>, <column>, <path to image>, <Resize image(default 32 by 32) VVVVVV
...,<width>, <height>
'''


Gui.image(win, 0, 0, "C:\\Users\\David\\Desktop\\photo.jpg", True, 32, 32)


'''
VVVV Fill a whole row with an array (Array length depends on how wide your grid is(default 6))
'''
samplearray = ["David Smerkous", "1", "7/11/15", "LS22", "78", ""]

Gui.setrow(win, samplearray, 1)  # fill a whole row 1


secondsample = ["Oliver Warne", "2", "7/13/15", "Collab space", "120", ""]

Gui.setrow(win, secondsample, 5)  # fill a whole row 5


'''
VVVVV Edit a whole column VVVVV
'''


columnsample = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

Gui.setcolumn(win, columnsample, 6, Gui.Label, 1)  # Fill a whole column each array num is a location on the column


'''
VVVV Edit individual boxes VVVVV
'''


Gui.changeentry(win, 2, 2, "Edit indv. item", Gui.Label)  # edit individual items

Gui.changeentry(win, 4, 3, "test button", Gui.Button, True, TESTBUTTON)  # Test button on the grid


'''
VVVV RUN THE ABOVE CODE FOREVER
'''


Gui.start()  # THIS CALL IS NECASSRY OR NO WINDOW WILL POP UP


'''
* Remember every change call needs to have the gui(root) with it
*
* Now after reading through this code try running it and see how they work with each other
'''
