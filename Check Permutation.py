def isPermutation(string1, string2) :    
    #Your code goes here
    sum1, sum2 = 0,0
    for i in string1:
        sum1 = sum1 + ord(i)
    for r in string2:
        sum2 = sum2 + ord(r)
    if sum1 == sum2:
        return 1
    return 0

#main
string1 = input()
string2 = input()

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

