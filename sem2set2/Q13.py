# Q13 Create a class called Ship that incorporates a ship’s number and location. Use the approach of problem 14 to
# number each ship object as it is created. Use two variables of the Angle class from problem 13 to represent the
# ship’s latitude and longitude. A method of the Ship class should get a position from the user and store it in the
# object; another should report the serial number and position. Write a main program that creates three ships, asks the
# user to input the position of each, and then displays each ship’s number and position.

class Angle:
    degrees:int
    minutes:float
    character:str
    format:str
    def __init__(self,deg=0,min=0,char=''):
        self.degrees=deg
        self.minutes=min
        self.character=char
    def set_angle(self):
        self.degrees=int(input('Enter Degrees: '))
        self.minutes=float(input('Enter Minutes: '))
        self.character=str(input('Enter Direction: '))
    def get_angle(self):
        self.format=str(self.degrees)+str('°')+str(self.minutes)+"'"+self.character

class Ship:
    count=0
    def __init__(self):
        Ship.count+=1
        self.serial=Ship.count

    def ship_report(self):
        print('Enter Longitude:')
        longitude=Angle()
        longitude.set_angle()
        longitude.get_angle()
        print('Enter Latitude:')
        latitude=Angle()
        latitude.set_angle()
        latitude.get_angle()
        print('I am Ship'+str(self.serial))
        print('My longitude is '+longitude.format)
        print('My latitude is '+latitude.format)

s1=Ship()
s2=Ship()
s3=Ship()
s1.ship_report()
s2.ship_report()
s3.ship_report()

