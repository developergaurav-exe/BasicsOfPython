



def removeAllOccurrencesOfChar(string,c):
    #Your code goes here.
    newword = str()
    for i in string:
        if i != c:
            newword = newword + i
    return newword


    










string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)
