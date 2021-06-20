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
d1=Date()
d1.set_date()
print(d1.get_date())
print(d1)
