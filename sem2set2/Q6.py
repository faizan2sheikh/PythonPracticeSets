class Vehicles:
    def __init__(self,wheel:int,clr:str,model:str):
        self.__noOfWheels=wheel
        self.__color=clr
        self.__modelNo=model

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
        
car=Vehicles(4,'white','AX345')
print(car.getModelNo())

car.setModelNo('CR456')
print(car.getModelNo())
