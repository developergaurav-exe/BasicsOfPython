class Rectangle:    
    # Write your code here.
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def getArea(self):
        print(self.l * self.b)

l, b = map(int, input().split())
obj = Rectangle(l,b)
obj.getArea()