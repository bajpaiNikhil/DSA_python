n = [1,2,2]

res = [[]]

for i in n:
    res +=[r + [i] for r in res]
print(res)