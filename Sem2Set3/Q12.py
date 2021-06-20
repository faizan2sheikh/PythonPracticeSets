class Engine:
    def __init__(self,number:str,date:None):
        self.__engineNo=number
        self.__dateOfManufacture=date

    def setEngineNo(self,number):
        self.__engineNo=number
    def getEngineNo(self):
        return self.__engineNo

    def setDateOfManufacture(self,date):
        self.__dateOfManufacture=date
    def getDateOfManufacture(self):
        return self.__dateOfManufacture

class Vehicles:
    def __init__(self,wheel:int,clr:str,model:str,engine):
        self.__noOfWheels=wheel
        self.__color=clr
        self.__modelNo=model
        self.engine_no=engine.getEngineNo()
        self.manu_date=engine.getDateOfManufacture()

    def setnoOfWheels(self,wheel):
        self.__noOfWheels=wheel
    def getnoOfWheels(self):
        return self.__noOfWheels

    def setColor(self,clr):
        self.__color=clr
    def getColor(self):
        return self.__color
        
    def setModelNo(self,model):
        self.__modelNo=model
    def getModelNo(self):
        return self.__modelNo

engine1=Engine('sfef23','23/34/2321')
v1=Vehicles(4,'white','AX345',engine1)
print(v1.manu_date)