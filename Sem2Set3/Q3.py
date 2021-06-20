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
    def get_data(self):
        self.last1=int(input('Enter last month sale: '))
        self.last2=int(input('Enter second last month sale: '))
        self.last3=int(input('Enter third last month sale: '))
    def put_data(self):
        print(f'last month sale: {self.last1}')
        print(f'second last month sale: {self.last2}')
        print(f'third last month sale: {self.last3}')        
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

p1=Publication('Alchemist',20)
p1.get_data()
p1.put_data()

b1=Book()
b1.get_data()
b1.put_data()

t1=Tape()
t1.get_data()
t1.put_data()