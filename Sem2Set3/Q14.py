class Engine:
    def __init__(self,number:str,date:str):
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
    def __str__(self):
        return f'''
                Class Vehicle
                Model no.: {self.__modelNo}
                No of wheels: {self.__noOfWheels}
                Color: {self.__color}
                Engine no: {self.engData.getEngineNo()}
                Date of manufacture (engine): {self.engData.getDateOfManufacture()}'''
    def __init__(self,wheel:int,clr:str,model:str):
        self.__noOfWheels=wheel
        self.__color=clr
        self.__modelNo=model

    def set_engineData(self,num,date):
        self.engData=Engine(num,date)

    def get_engineData(self):
        return f'Engine Number is {self.engData.getEngineNo()} and date of manufacturing is {self.engData.getDateOfManufacture()}'

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


v1=Vehicles(4,'white','AX345')
v1.set_engineData('sfef23','23/04/2021')
print(v1)