#Your code goes here
import math
s = int(input())
e = int(input())
w = int(input())
for i in range(s, e+1, w): 
    f = (i - 32)*5/9 
    if f < 0:
        print(i, math.ceil(f))
    elif f >=0:
        print(i, math.floor(f))

























