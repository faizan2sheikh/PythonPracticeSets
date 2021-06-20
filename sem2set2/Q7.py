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

e1=Engine('234khn4k','22dec2001')

print(e1.getEngineNo())
print(e1.getDateOfManufacture())

e1.setEngineNo('ghj13g23')
e1.setDateOfManufacture('23mar2001')
print(e1.getEngineNo())
print(e1.getDateOfManufacture())