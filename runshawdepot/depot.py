class Depot():
    def __init__(self, name, location, supervisor):
        self.name = name
        self.location = location
        self.supervisor = supervisor
    
    def getname(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getLocation(self):
        return self.location
    
    def setLocation(self, location):
        self.location = location

    def getSupervisor(self):
        return self.supervisor
    
    def setSupervisor(self, supervisor):
        self.supervisor = supervisor

class DepotList():
    depots = []

    def __init__(self):
        self.filename = "depots.txt"

    def searchDepots(self):
        pass

    def writeDepots(self):
        pass

    def readDepots(self):
        pass