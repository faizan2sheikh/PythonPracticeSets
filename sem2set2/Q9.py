class TollBooth:
    def __init__(self):
        self.cars_passed=0
        self.amount=0
        self.payCar=0
        self.NotPayCar=0
    def payingCar(self):
        self.cars_passed+=1
        self.amount+=50
        self.payCar+=1
    def NoPayCar(self):
        self.cars_passed+=1
        self.NotPayCar+=1
    def display(self):
        return self.cars_passed,self.amount,self.payCar,self.NotPayCar

first=TollBooth()
first.payingCar()
first.payingCar()
first.payingCar()
first.NoPayCar()
first.payingCar()
first.NoPayCar()
first.payingCar()

print(first.display())
