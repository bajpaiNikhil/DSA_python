arr = [1, 4, 13,-3 , -10, 5]
# so the idea is to keep a prefix sum hashset and if the value in it repeats
# itself then there is a subarray with zero sum else not
# only cornor case is is prefix sum is zero itself .

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
