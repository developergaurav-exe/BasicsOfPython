class Square:
    l =10
    def __init__(self, l):
        self.l = l
    
    def area(self):
        print(self.l * self.l)

i = int(input())
ob = Square(i)
ob.area()