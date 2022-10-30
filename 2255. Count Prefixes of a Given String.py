words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"

# print(map(s.startswith,words))
# l = list(map(s.startswith,words))
# for i in l:
#     print(i)
# print(l)
count = 0
for i in words:
    print(i , s[:len(i)])
    if i == s[:len(i)]:
        count+=1
print(count)