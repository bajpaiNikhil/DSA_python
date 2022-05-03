arr = [1, 4, 13, -10, 5]


def zeroSum(arr):
    hashSet = set()
    prefix = 0
    for i in arr:
        prefix = prefix + i
        if prefix in hashSet:
            return True
        if prefix == 0:
            return True
        hashSet.add(prefix)
    return False


print(zeroSum(arr))
