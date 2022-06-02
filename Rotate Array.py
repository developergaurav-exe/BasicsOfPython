#Your code goes here.
n = int(input())
l = list(map(int, input().split()))
k = int(input())
arr = []
for i in range(0,k):   
    arr.append(l[i])

rlist = l + arr
l = rlist[k::]
for a in l:
    print(a, end = " ")




















