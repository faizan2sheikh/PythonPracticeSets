from abc import ABCMeta,abstractmethod
class Polygon(metaclass=ABCMeta):
    def __init__(self,side,lengthsList):
        self.noOfside=side
        self.lengths=lengthsList
    def perimeter(self):
        self.per=0
        for i in self.lengths:
            self.per+=int(i)
        return self.per
    @abstractmethod
    def getLengths(self):
        pass

# p=Polygon(3,[23,4,65])
# print(p.lengths)
# print(p.getLengths())