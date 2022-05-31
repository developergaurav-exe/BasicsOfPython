#Write your printDivisors function here.
def printDivisors(d):
    if d == 0:
        print("0")
    else:
        print("1", end = " ")
        for i in range(2,d):
            if(d%i == 0):
                print(i,end = " ")
        print(d)

n = int(input())
printDivisors(n)
