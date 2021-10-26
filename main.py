import runshawdepot
from tkinter import *


class MyDepot():
    def __init__(self, window, dlist):

        # set the list classe
        self.driverlist = dlist

        # set all the frames
        self.a_frame = Frame(window)
        self.b_frame = Frame(window)

        # build all the frames
        self.setFrameA()
        self.setFrameB()


    def setFrameA(self):
        self.lbl_one = Label(self.a_frame, text="a frame")
        self.lbl_one.pack()
        self.btn_toBFrame = Button(self.a_frame, text= "go to b frame", command =self.goBframe)
        self.btn_toBFrame.pack()
        self.a_frame.pack()

    def setFrameB(self):
        self.lbl_two = Label(self.b_frame, text="b frame")

        self.lbl_two.pack()

        self.etr_one = Entry(self.b_frame)
        self.etr_two = Entry(self.b_frame)
        self.etr_three = Entry(self.b_frame)
        self.etr_four = Entry(self.b_frame)
        self.etr_five = Entry(self.b_frame)

        self.lbl_forename = Label(self.b_frame, text="Forename")
        self.lbl_surname = Label(self.b_frame, text="Surname")
        self.lbl_address = Label(self.b_frame, text="Address")
        self.lbl_role = Label(self.b_frame, text="Role")
        self.lbl_depot = Label(self.b_frame, text="Depot")
        self.btn_submit = Button(self.b_frame, text= "submit customer info", command =self.submit)

        self.lbl_forename.pack()
        self.etr_one.pack()
        self.lbl_surname.pack()
        self.etr_two.pack()
        self.lbl_address.pack()
        self.etr_three.pack()
        self.lbl_role.pack()
        self.etr_four.pack()
        self.lbl_depot.pack()
        self.etr_five.pack()
        self.btn_submit.pack()

        self.btn_toAFrame = Button(self.b_frame, text= "go to a frame", command =self.goAframe)
        self.btn_toAFrame.pack()

    def goBframe(self):
        self.a_frame.pack_forget()
        self.b_frame.pack()

    def goAframe(self):
        self.b_frame.pack_forget()
        self.a_frame.pack()

    def submit(self):
        drvforename = self.etr_one.get()
        drvsurname = self.etr_two.get()
        drvaddress = self.etr_three.get()
        drvrole = self.etr_four.get()
        drvdepot = self.etr_five.get()

        drv = runshawdepot.Driver(drvforename, drvsurname, drvaddress, drvrole, drvdepot)
        self.driverlist.addDriver(drv)

        self.etr_one.delete(0,END)
        self.etr_two.delete(0,END)
        self.etr_three.delete(0,END)
        self.etr_four.delete(0,END)
        self.etr_five.delete(0,END)

        # prints out the drivers in the list each time one is added 
        # for testing purposes.
        for peeps in self.driverlist.drivers:
            print(peeps.toString())


def main():
    # create a new window
    window = Tk()

    # create an instance of the DriverList 
    # to pass into the MyDepot class
    driverList = runshawdepot.DriverList()

    #create a new MyDepot instance and pass in the window 
    # and the driver list.
    MyDepot(window, driverList)

    window.mainloop()


if __name__ == '__main__':
    main()









