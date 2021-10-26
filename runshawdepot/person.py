class Person():
    def __init__(self, forename, surname, address, role):
        self.forename = forename
        self.surname = surname
        self.address = address
        self.role = role
    
    def getForename(self):
        return self.forename
    
    def setForname(self, name):
        self.forename = name

    def getSurname(self):
        return self.surname
    
    def setSurname(self, name):
        self.surname = name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address

    def getRole(self):
        return self.role
    
    def setRole(self, role):
        self.role = role
    
# class Driver inherits from the class Person. 
# this is why Person is a parameter in the brackets
class Driver(Person):
    def __init__(self, forename, surname, address, role, depot):
        # super().__init__ calls the constructor from the super class
        # This is the Person class. 
        # The parameters forename, surname, address and role are all dealt with 
        # in the super class. Depot is assigned below this.
        super().__init__(forename, surname, address, role) 
        self.depot = depot
    
    # As Person has no attribute depot the getter and setter must be 
    # Defined in this class.
    def getDepot(self):
        return self.depot
    
    def setDepot(self, depot):
        self.depot = depot

    def toString(self):
        return self.forename + "," + self.surname + "," + self.address + "," +  self.role + "," + self.depot

class DriverList():
    # this attribute, drivers, is above the constructor.
    # It does not have self in front of it.
    # This means it is common to all instances of the DriverList class.
    # All instances of DriverList access the same drivers list.
    # drivers is a class or static variable.
    drivers = []
    def __init__(self):
        self.filename = "drivers.txt"
        
    def addDriver(self, driver):
        self.drivers.append(driver)
    
    def printList(self):
        for item in self.drivers:
            print(item.toString())
    
    def searchdriver(self, driverID):
        pass

    def sortdrivers(self):
        pass

    def writeToFile(self):
        pass

    def readFromFile(self):
        pass


class Supervisor(Person):
    def __init__(self, forename, surname, address, role, grade):
        super().__init__(forename, surname, address, role)
        self.grade = grade
    
    def getGrade(self):
        return self.grade
    
    def setGrade(self, grade):
        self.depot = grade


def main():
    # create a new instance of Person
    peep = Person("john","connor","19828 valerio street","driver")

    # print that Persons forename
    print(peep.getForename(), "This is accessed from the getter.")
    print(peep.forename, "This is accessed using the instance variable itself.")

    # create a new instance of Driver and Supervisor
    drv1 = Driver("andrew","clark","athlete road","driver","liverpool")
    drv2 = Driver("Brian","Johnson","brain crescent","driver","Preston")
    sup1 = Supervisor("claire","standish","princess avenue","supervisor","3")

    # prints out the Drivers depot and type
    print("drv1s depot is:" , drv1.getDepot())
    print("drv1 is type:", type(drv1))

    # prints out the SUpervisors grade and type
    print("sup1s grade is:", sup1.getGrade())
    print("sup1s type is:", type(sup1))

    # create an instance of DriveList to store the drivers
    aListofDrivers = DriverList()
    # add 2 drivers to the list 
    aListofDrivers.addDriver(drv1)
    aListofDrivers.addDriver(drv2)

    # print out all the drivers names in the list
    # for item in aListofDrivers.drivers:
    #     print(item.toString())
    
    # printing the list of drivers
    # using the method in the list class
    aListofDrivers.printList()



if __name__ == "__main__":
    main()
        


    # driver1 = Driver("eric","halfabee","21 lane","driver","liverpool")
    # print(driver1.getForename())
    # sup1 = Supervisor("janet","wheels","45 egg road","supervisor","4")
    # print(sup1.getForename(),sup1.getGrade())