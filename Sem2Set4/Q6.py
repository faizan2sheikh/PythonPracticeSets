from abc import ABCMeta,abstractmethod
class Polygon(metaclass=ABCMeta):
    def __init__(self,side):
        self.noOfside=side
    @abstractmethod
    def getLengths(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self,lenList):
        super().__init__(4)
        self.lengths=lenList
    def getLengths(self):
        return self.lengths
    def area(self):
        return self.lengths[0]*self.lengths[1]
    def perimeter(self):
        return 2*(self.lengths[0]+self.lengths[1])

r=Rectangle([4,5])
print(r.getLengths())
print(r.area())
print(r.perimeter())