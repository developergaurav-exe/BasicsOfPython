#Write your countBits function here.
def countBits(b):
    count = 0
    if b == 0:
        return 0
    elif b>0:
        bits = []
        while(b>0):
            one = b%2
            bits.append(one)
            b = b//2
        for i in bits:
            if i == 1:
                count = count + 1

        return count

n = int(input())
print(countBits(n))

