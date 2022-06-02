
def reverseStringWordWise(string):
    #Your code goes here
    newword = []
    word = string.split()
    for i in word[::-1]:
        newword.append(i)
    return newword

string = input()
ans = reverseStringWordWise(string)
print(*ans)