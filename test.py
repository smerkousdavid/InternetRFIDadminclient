from LTS import *
from gui import Gui
from time import sleep
import threading

def start():
    while True:
        print "start"
        count = 1
        learnerarray = []
        for i in range(0,5):
            learnerarray.append(LTSBackend(count).getData())
            count = count + 1

        count = 1
        for i in learnerarray:
            Gui.setrow(win,i,count)
            count = count + 1
        sleep(10)

win = Gui()
Gui.setdefault(win)

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


count = 1
learnerarray = []
for i in range(0,5):
    learnerarray.append(LTSBackend(count).getData())
    count = count + 1

count = 1
for i in learnerarray:
    Gui.setrow(win,i,count)
    count +=1

t = threading.Thread(target=start)
t.start()
Gui.start()
