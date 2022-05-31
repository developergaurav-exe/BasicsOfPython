#import CheckingPrime
#Write your totalPrime function here.
def is_prime(n):
    if n == 0:
        return 0
    elif n>0:
        for i in range(2,n):
            if n%i == 0:
                return 0
        
    return 1

def totalPrime(S,E):
    count = 0
    for i in range(S,E+1):
        if is_prime(i) == 1:
            count = count + 1
    
    return count
    
#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))


