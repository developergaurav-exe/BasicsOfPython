from sys import stdin
def reverseEachWord(string) :    
    #Your code goes here.
    return ' '.join(word[::-1] for word in string.split(" "))


#main
string = stdin.readline().strip()
ans = reverseEachWord(string)
print(ans)
