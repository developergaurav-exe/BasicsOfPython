def fibonacciNumber(n):
    # Write your code here.
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

choice = int(input())
fibonacciNumber(choice)

'''
    Time Complexity: O(log(N)).
    Space Complexity: O(log(N)).

    Where 'N' is the given integer.


def multiply(a, b):
    
    mod = int(1e9 + 7)
    c = [[0 for i in range(2)] for j in range(2)]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][k] = (c[i][k] + a[i][j] * b[j][k]) % mod
                
    return c

# Function to calclate n'th power of a matrix.
def matrix_power(coef, n):
    
    # To store the resultant matrix.
    res = [[1, 0], [0, 1]]
    
    # While loop till n > 0.
    while n > 0:
        
        # If n is odd, multiply res with coef.
        if (n % 2 != 0):
            res = multiply(res, coef)
            
        # Multiply coef with coef and update n to n//2.
        coef = multiply(coef, coef)
        n //= 2
        
    return res

def fibonacciNumber(n):
    
    coef = [[0, 1], [1, 1]]
    
    # Calculating the (n-1)th power of the coef matrix.
    res = matrix_power(coef, n - 1)
    
    # Return the bottom right element of the resultant matrix.
    return res[1][1]
'''        