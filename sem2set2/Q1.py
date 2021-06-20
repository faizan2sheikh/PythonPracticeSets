class Circle:
    radius=None
    color=None
    def setRadius(self,r):
        self.radius=r
    def getRadius(self):
        return self.radius
    def setColor(self,c):
        self.color=c
    def getColor(self):
        return self.color
    def getCircumference(self):
        return 2*3.142*self.radius
    def getArea(self):
        return 3.142*(self.radius**2)

c=Circle()
c.setRadius(5)
c.setColor('white')
print(c.getCircumference())
print(c.getArea())