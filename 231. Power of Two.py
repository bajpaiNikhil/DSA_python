n=3

setBit = 0
while n>0:
    if (n & 1)==1:
        setBit+=1
    n=n>>1
print(setBit)