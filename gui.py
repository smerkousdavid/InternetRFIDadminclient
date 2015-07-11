from Tkinter import Tk, Button, Label, Text, Entry, Radiobutton, mainloop


class Gui:

    Button = Button
    Label = Label
    Text = Text
    Entry = Entry
    Radiobutton = Radiobutton

    def __init__(self):
        self.root = Tk()
        self.height = None
        self.width = None

    def changeentry(self, row, column, text, types=Label, callback=False, callname=None):
        if types is Button and callback:
            Button(self.root, text=text, command=callname).grid(row=row, column=column)
        else:
            types(self.root, text=text).grid(row=row, column=column)

    def setgridsize(self, height=5, width=6):
        self.height = height
        self.width = width
        for i in range(1, height):  # Rows
            for j in range(width):  # Columns
                b = Entry(self.root, text="")
                b.grid(row=i, column=j)

    def settitle(self, text="Academy Management System"):
        self.root.wm_title(text)

    def control(self, location=None, name=None, year=None, date=None):
        Button(self.root, text="  Location   ", command=location, bg="#297ACC").grid(row=1, column=0)
        Button(self.root, text="    Name     ", command=name, bg="#297ACC").grid(row=3, column=0)
        Button(self.root, text="    Year     ", command=year, bg="#297ACC").grid(row=5, column=0)
        Button(self.root, text="    Date     ", command=date, bg="#297ACC").grid(row=7, column=0)

    def setdefault(self):
        for i in range(1, 10):  # Rows
            for j in range(1, 7):  # Columns
                b = Entry(self.root, text="")
                b.grid(row=i, column=j)
        self.height = 9
        self.width = 6
        self.root.wm_title("Academy Management System")
        Label(self.root, text="Name").grid(row=0, column=1)
        Label(self.root, text="Year").grid(row=0, column=2)
        Label(self.root, text="Time checked").grid(row=0, column=3)
        Label(self.root, text="Location").grid(row=0, column=4)
        Label(self.root, text="Id").grid(row=0, column=5)
        Label(self.root, text="Rfid").grid(row=0, column=6)

    def getcolumns(self):
        return self.width

    def getrows(self):
        return self.height

    def setrow(self, array, rownum, type=Label, start=1):
        for at in range(len(array)):
            type(self.root, text=array[at]).grid(row=rownum, column=at+start)

    def setcolumn(self, array, columnnum, type=Label, start=1):
        for at in range(len(array)):
            type(self.root, text=array[at]).grid(row=at+start, column=columnnum)

    def clearrow(self, rownum):
        for clear in range(1, self.width+1):
            Entry(self.root, text="").grid(row=rownum, column=clear)

    def clearcolumn(self, columnnum):
        for clear in range(1, self.height+1):
            Entry(self.root, text="").grid(row=clear, column=columnnum)

    def cleargrid(self):
        for c in range(1, self.width+1):
            for r in range(1, self.height+1):
                Entry(self.root, text="").grid(row=r, column=c)

    def deleteentry(self, row, column):
        Entry(self.root, text="").grid(row=row+1, column=column+1)

    @staticmethod
    def start():
        mainloop()
