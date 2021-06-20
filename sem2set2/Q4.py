class Worker:
    __hoursWorked=None
    __wageRate=None

    def setHoursWorked(self,h):
        self.__hoursWorked=int(h)
    def changeRate(self,r):
        self.__wageRate=int(r)
    def pay(self):
        return self.__wageRate*self.__hoursWorked


w1=Worker()
w1.setHoursWorked(5)
w1.changeRate(10)
print(w1.pay())