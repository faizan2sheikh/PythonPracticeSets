class Point:
    def __init__(self,p1,p2):
        self.point1=p1
        self.point2=p2
    def set_points(self,p1,p2):
        self.point1=p1
        self.point2=p2
    def __str__(self):
        return f'({self.point1},{self.point2})'