from abc import ABCMeta,abstractmethod
class Polygon(metaclass=ABCMeta):
    def __init__(self,side):
        self.noOfside=side
    @abstractmethod
    def getLengths(self):
        pass
class Triangle(Polygon):
    def __init__(self,lenList):
        super().__init__(3)
        self.lengths=lenList
    def perimeter(self):
        self.per=0
        for i in self.lengths:
            self.per+=int(i)
        return self.per
    def getLengths(self):
        return self.lengths

base=4
height=7
t=Triangle([base,height,65**0.5])
print(t.perimeter())
print(t.getLengths())