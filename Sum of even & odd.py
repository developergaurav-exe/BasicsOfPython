#Your code goes here
n = input()
r = [int(a) for a in str(n)]
evensum, oddsum = 0,0
for i in r:
    if(i%2 == 0):
        evensum = evensum + i
    else:
        oddsum = oddsum + i
print(evensum, oddsum)























