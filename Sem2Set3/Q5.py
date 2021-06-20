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
    def __init__(self,l1=0,l2=0,l3=0):
        self.last1=int(l1)
        self.last2=int(l2)
        self.last3=int(l3)
    def get_data(self):
        self.last1=int(input('Enter last month sale: '))
        self.last2=int(input('Enter second last month sale: '))
        self.last3=int(input('Enter third last month sale: '))
    def put_data(self):
        print(f'Last month sale: {self.last1}')
        print(f'Second last month sale: {self.last2}')
        print(f'Third last month sale: {self.last3}')        
class Book(Publication):
    pageCount:int
    record=Sales()
    def get_data(self):
        self.pageCount=int(input('Enter Page Count: '))
    def put_data(self):
        print(f'Publication\'s Page Count is {self.pageCount}')
class Tape(Publication):
    record=Sales()
    playingTime:float
    def get_data(self):
        self.playingTime=float(input('Enter playing time: '))
    def put_data(self):
        print(f'Publication\'s playing time is {self.playingTime}')

b1=Book('Akon',24)
b1.record.get_data()
b1.record.put_data()