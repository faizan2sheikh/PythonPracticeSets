class Point:
    def __init__(self,x,y):
        self.pointx=int(x)
        self.pointy=int(y)
    def set_points(self,x,y):
        self.pointx=int(x)
        self.pointy=int(y)
    def __str__(self):
        return f'({self.pointx},{self.pointy})'

class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.point1=Point(x1,y1)
        self.point2=Point(x2,y2)
    def findDistance(self):
        return f'Distance between the points is {((self.point2.pointx-self.point1.pointx)^2+(self.point2.pointy-self.point1.pointy)^2)^int(0.5)}'

d1=Distance(23,23,324,44)
print(d1.findDistance())