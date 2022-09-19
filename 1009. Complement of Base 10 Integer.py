n = 37
#Naive approach
# ans = ""
# while n > 0:
#     ans += str(n % 2)
#     n = n // 2
# binary = ans[::-1]
# print(binary)
# ans = ""
# for i in binary:
#     ans += "0" if i == "1" else "1"
# print(ans)
# print(int(ans,2))
c = 1
while n>c:
    c = (c<<1)|1

print(c^n)