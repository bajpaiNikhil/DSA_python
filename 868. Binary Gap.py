n = 38
ans = ""
while n>0:
    ans+=str(n%2)
    n = n//2
binary = ans[::-1]
print(binary)
des = prev = 0
for i , j in enumerate(binary):
    print(i , j)
    if j == "1":
        des = max(des , i-prev)
        prev=i
print(des)
