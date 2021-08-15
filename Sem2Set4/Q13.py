from abc import ABCMeta,abstractmethod
class Polygon(metaclass=ABCMeta):
    def __init__(self,side):
        self.noOfside=side
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def getLengths(self):
        pass

class Triangle(Polygon):
    def __init__(self,lenList):
        super().__init__(3)
        self.lengths=lenList
    def getLengths(self):
        return self.lengths
    def area(self):
        try:
            a=self.lengths[0]
            b=self.lengths[1]
            c=self.lengths[2]
            s= (a + b + c)/2
            return (s*(s-a)*(s-b)*(s-c))**0.5
        except:
            return 'Some side value is not integer'
    def perimeter(self):
        try:
            return (self.lengths[0]+self.lengths[1]+self.lengths[2])
        except:
            return 'Some side value is not integer'

class Rectangle(Polygon):
    def __init__(self,lenList):
        super().__init__(4)
        self.lengths=lenList
    def getLengths(self):
        return self.lengths
    def area(self):
        try: 
            return self.lengths[0]*self.lengths[1]
        except:
            return 'Some side value is not integer'
    def perimeter(self):
        try:
            return 2*(self.lengths[0]+self.lengths[1])
        except:
            return 'Some side value is not integer'

t=Triangle([3,'f',5])
print(t.getLengths())
print(t.perimeter())
print(t.area())

r=Rectangle([4,5])
print(r.getLengths())
print(r.area())
print(r.perimeter())