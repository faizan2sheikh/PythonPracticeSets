class Int:
    def __init__(self,v:int=0):
        self.var=v
    def change(self,newV):
        self.var=newV
    def display(self):
        print(self.var)
    def add(self,another):
        if type(another)==Int:
            return self.var+another.var
        else: 
            print('Unsupported Argument')

n1=Int(7)
n2=Int(9)
result=n1.add(n2)
n3=Int()
n3.change(result)
n3.display()