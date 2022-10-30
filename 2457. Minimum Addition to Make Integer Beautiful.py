n = 467
target = 6

print(sum(map(int, str(n))))


def sumOfDigit(n):
    summ = sum(map(int, str(n)))
    return summ


mull = 1
add = 0
while sumOfDigit(n + add) > target:
    mull = mull * 10
    add = mull - n % mull
print(add)
