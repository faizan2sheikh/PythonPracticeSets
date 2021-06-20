class Time:
    def __init__(self,h:int=0,m:int=0,s:int=0):
        if h<24:self.hours=h
        else: print('Invalid hours')
        if m<60:self.minutes=m
        else: print('Invalid minutes')
        if s<60:self.seconds=s
        else: print('Invalid seconds')

    def displayTime(self):
        self.formatted = str(self.hours)+':'+str(self.minutes)+':'+str(self.seconds)
        return self.formatted

    def addTime(self,t2):
        if type(t2)==Time:
            pass

t1=Time(12,34,32)
t2=Time(10,23,34)
print(t1.displayTime())