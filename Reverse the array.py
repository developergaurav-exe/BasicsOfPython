#Your code goes here.
n = int(input())
l = list(map(int, input().split()))
rl = [a for a in l[::-1]]
for i in rl:
    print(i, end = " ")
