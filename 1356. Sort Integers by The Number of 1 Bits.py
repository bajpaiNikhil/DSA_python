from collections import defaultdict

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

dic = defaultdict(list)


def countBits(n):
    res = 0
    while n > 0:
        res += 1
        n = n & (n - 1)
    return res


print(countBits(8))

ans = sorted(arr, key=lambda x: (countBits(x), x))
print(ans)
