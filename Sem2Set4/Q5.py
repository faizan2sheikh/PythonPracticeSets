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
class Triangle(Polygon):
    def __init__(self,lenList):
        super().__init__(3)
        self.lengths=lenList
    def getLengths(self):
        return self.lengths
    def area(self):
        a=self.lengths[0]
        b=self.lengths[1]
        c=self.lengths[2]
        s= (a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5

t=Triangle([3,4,5])
print(t.getLengths())
print(t.area())