class Polygon:
    def __init__(self,side,lengthsList):
        self.noOfside=side
        self.sideLengthList=lengthsList
    def perimeter(self):
        self.per=0
        for i in self.sideLengthList:
            self.per+=int(i)
        return self.per
    @property
    def lengths(self):
        'contain lengths'
        return self.sideLengthList
    @lengths.setter
    def lengths(self,lenList):
        self.sideLengthList=lenList
    @lengths.deleter
    def lengths(self):
        self.sideLengthList=[]
        print('Deleted!')

p=Polygon(3,[23,4,65])
p.lengths=[7,43,41]
del(p.lengths)
print(p.lengths)