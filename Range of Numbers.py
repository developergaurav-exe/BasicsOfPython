def total(S,E):
    l = []
    for i in range(S,E+1):
        l.append(i)
    return l


#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(total(S,E))