def is_prime(n):
    if n == 0:
        return 0
    elif n>0:
        for i in range(2,n):
            if n%i == 0:
                return 0
        
    return 1

n = int(input())
print(is_prime(n))    