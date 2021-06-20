class Publication:
    title:str
    price:float
    def __init__(self,title='Unknown',price=0):
        self.title=str(title)
        self.price=float(price)
        self.d=Date()
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
        print(f'last month sale: {self.last1}')
        print(f'second last month sale: {self.last2}')
        print(f'third last month sale: {self.last3}')   
class Date:
    day:str
    month:str
    year:str
    date:str
    format=int(input('''Enter the format:
    1:dd-mm-yy
    2:mm/dd/yy
    3:mm_name dd,yy
    '''))
    if format==1:
        def __str__(self):
            date=f'Today the date is {self.day}-{self.month}-{self.year}'
            return date
    if format==2:
        def __str__(self):
            date=f'Today the date is {self.month}-{self.day}-{self.year}'
            return date
    if format==3:
        def __str__(self):
            date=f'Today the date is {self.month} {self.day},{self.year}'
            return date

    def set_date(self):
        self.day=input("Enter Day: ")
        self.month=input("Enter Month: ")
        self.year=input("Enter Year: ")
    def get_date(self):
        return self     
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

b1=Book()
b1.get_data()
b1.put_data()
b1.get_d
print(b1.d)

# t1=Tape()
# t1.get_data()
# t1.put_data()