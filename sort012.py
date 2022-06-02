def sort012(arr):
    #Your code goes here.
    ar0, ar1, ar2 = [],[],[]
    if len(arr) <= 1:
        return
    arr.sort()
    return arr    
    
    

#Driver's code
t = int(input())

while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    sort012(arr)
    print(*arr)
    
    t -= 1

    
