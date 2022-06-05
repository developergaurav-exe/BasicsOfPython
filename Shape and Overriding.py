class Shape:

    def printMyType(self):
        pass



class Sqaure(Shape):
    def __init__(self,l):
        self.l = l

    def calculateArea(self):
        print(self.l**2)

    def printMyType(self):
        print('square')

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
 
    def calculateArea(self):
        print(self.l * self.b)
    
    def printMyType(self):
        print('rectangle')

#driver code
obj1 = Sqaure(5)
obj1.printMyType()
obj1.calculateArea()


obj2 = Rectangle(5,4)
obj2.printMyType()
obj2.calculateArea()
