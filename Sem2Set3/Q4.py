class Publication:
    title:str
    price:float
    def __init__(self,title,price):
        self.title=str(title)
        self.price=float(price)        
    def get_data(self):
        self.title=str(input('Enter title: '))
        self.price=float(input('Enter price: '))
    def put_data(self):
        print(f'Publication name is {self.title}')
        print(f'Publication price is {self.price}')
class Sales:
    last1:float
    last2:float
    last3:float
    def __init__(self,l1,l2,l3):
        self.last1=int(l1)
        self.last2=int(l2)
        self.last3=int(l3)
    def get_data(self):
        self.last1=int(input('Enter last month sale: '))
        self.last2=int(input('Enter second last month sale: '))
        self.last3=int(input('Enter third last month sale: '))
    def put_data(self):
        print(f'last month sale: {self.last1}')
        print(f'second last month sale: {self.last2}')
        print(f'third last month sale: {self.last3}')        
class Disk(Sales,Publication):
    def __init__(self,l1,l2,l3,title,price):
        Sales.__init__(self,l1,l2,l3)
        Publication.__init__(self,title,price)
    diskType:str
    def get_data(self):
        Disktype={'c':'CD','d':'DVD'}
        disk_in=input('Enter Disk type: ')
        self.diskType=Disktype[disk_in]
    def put_data(self):
        print(f'Disk type is {self.diskType}')
class Book(Sales,Publication):
    pageCount:int
    def get_data(self):
        self.pageCount=int(input('Enter Page Count: '))
    def put_data(self):
        print(f'Publication\'s Page Count is {self.pageCount}')
class Tape(Sales,Publication):
    playingTime:float
    def get_data(self):
        self.playingTime=float(input('Enter playing time: '))
    def put_data(self):
        print(f'Publication\'s playing time is {self.playingTime}')

d1=Disk(24,32,24,'ALchemist',500)
d1.get_data()
d1.put_data()