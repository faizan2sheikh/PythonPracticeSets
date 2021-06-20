class BasicSalary:
    basicSal:int
    def __init__(self,BasicSal):
        self.basicSal=BasicSal
    def annualBasicSalary(self):
        return self.basicSal*12
class Employee:
    def __init__(self,ann_bon,basic):
        self.bas=BasicSalary(basic)
        self.annualBonus=ann_bon
    def annualNetSalary(self):
        print(self.bas.annualBasicSalary()+self.annualBonus)

e1=Employee(50000,35000)
e1.annualNetSalary()

# relationship is composition