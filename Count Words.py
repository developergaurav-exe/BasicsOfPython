from sys import stdin
def countWords(string) :
    count = 0
    # Your code goes here
    for i in string:
        if i == " " or i == "/n":
            count +=1
    return count+1

#main
string = stdin.readline().strip();
count = countWords(string)

print(count)

