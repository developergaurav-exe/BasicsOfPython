import math
from math import gcd
class Fraction:

    # Create your fraction class here.
    def __init__(self, num, den=1):
        self.num = num
        self.den = den


    def simplify(self):
        gcd = math.gcd(int(self.num), int(self.den))
        self.num /= gcd
        self.den /= gcd


    def __add__(self, object2):
        ansNum = (self.num * object2.den + object2.num * self.den)
        ansDen = self.den * object2.den
        self.num = ansNum
        self.den = ansDen
        self.simplify()


    def __mul__(self, object2):
        self.num *= object2.num
        self.den *= object2.den
        self.simplify()


    def print(self):
        print('{}/{}'.format(int(self.num),int(self.den)))
        

# Driver code goes here.

num1,den1 = map(int, input().split())


fraction1 = Fraction(num1, den1)

queries = int(input())

for i in range(0, queries):
    typeOfOperation , num2 , den2 = map(int, input().split())

    fraction2 = Fraction(num2, den2)
    if (typeOfOperation == 1):

        fraction1+fraction2
        fraction1.print()
    elif (typeOfOperation == 2):

        fraction1*fraction2
        fraction1.print()