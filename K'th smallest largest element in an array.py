def kthSmallestLargest(arr, k):
    new = []

    for i in arr:

       if i not in new:

            new.append(i)

    new.sort()

    if len(new) < k:

        return -1, -1

    return new[k - 1], new[k] 
    
    

#Driver's code
t = int(input())

while t > 0:
    
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    small,large = kthSmallestLargest(arr,k)
    print(large,small)
    
    t -= 1
