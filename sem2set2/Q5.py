class Worker:
    def __init__(self,h=None,r=None):
        self.__hoursWorked=h
        self.__wageRate=r
        
    def pay(self):
        return self.__wageRate*self.__hoursWorked
w1=Worker(4,9)
print(w1.pay())