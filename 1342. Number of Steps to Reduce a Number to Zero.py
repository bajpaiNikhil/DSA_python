n= 8
res = 0

while n>0:
    if n&1 == 0:
        res+=1
    else:
        res+=2
    n = n>>1
print(res-1)