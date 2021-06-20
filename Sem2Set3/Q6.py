class Date:
    day:int
    month:int
    year:int
    date=''
    def __str__(self):
        date=f'Today the date is {self.day}/{self.month}/{self.year}'
        self.date=date
        return date

    def set_date(self):
        self.day=int(input("Enter Day: "))
        self.month=int(input("Enter Month: "))
        self.year=(input("Enter Year: "))
    def get_date(self):
        date=f'Today the date is {self.day}/{self.month}/{self.year}'
        return date
d1=Date()
d1.set_date()
print(d1.get_date())
print(d1)
