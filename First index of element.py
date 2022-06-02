#Your code goes here.
n = int(input())

l = list(map(int,input().strip().split()))[:n]

x = int(input())

def search(l,x):
    for i in l:
        if i == x:
            print(l.index(i))
            break
        elif x not in l:
             print("-1")
             break

search(l,x)