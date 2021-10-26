class Vehicle():
    def __intit__(self, reg, make, model,depot):
        self.vreg = reg
        self.vmake = make
        self.vmodel = model
        self.vdepot = depot
    
    def getVreg(self):
        return self.vreg
    
    def setVreg(self, reg):
        self.vreg = reg

    def getVmake(self):
        return self.vmake
    
    def setVmake(self, make):
        self.vmake = make
    
    def getVmodel(self):
        return self.vmodel
    
    def setVmodel(self, model):
        self.model = model

    def getVdepot(self):
        return self.vdepot
    
    def setVdepot(self, depot):
        self.vdepot = depot


class VehicleList():
    vehicles = []

    def __init__(self):
        self.filename = "vehicles"
    
    def searchVehicles(self):
        pass

    def saveVehicles(self):
        pass

    def readVehicles(self):
        pass

    

