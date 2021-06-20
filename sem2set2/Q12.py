# Then write a main program that creates three objects and queries each one about its serial number.
# They should respond I am object number 2, and so on.

class Tracker:
    count=0
    def __init__(self):
        Tracker.count+=1
        self.serial=Tracker.count
    def Serial_no(self):
        print('I am object number',self.serial)
    
o1=Tracker()
o1.Serial_no()
o2=Tracker()
o2.Serial_no()
o3=Tracker()
o3.Serial_no()