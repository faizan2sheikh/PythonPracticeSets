# Write code to create a class called Time that has separate member data for hours, minutes, and seconds. Make
# constructor to initialize these attributes, with 0 being the default value. Add a method to display time in 11:59:59
# format. Add another method addTime which takes one argument of Time type and add this time to the current time
# of the self object. Instantiate two objects t1 and t2 to any arbitrary values, display both the objects, add t2 to t1
# and display the result.

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
