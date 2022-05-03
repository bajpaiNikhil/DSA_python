arr = [5, 8, 6, 13, 3, -1]
target = 22
# prefix_sum = [5 , 13 , 19  , 32 , 35 , 34 ]
# the idea is to check is the prefix_sum contain duplicates when elements is substracted by target
def givenSum(arr, target):
    hashSet = set()
    prefix = 0

    for i in arr:
        prefix = prefix+i
        if (prefix-target) in hashSet:
            return True
        if prefix == target:
            return True
        hashSet.add(prefix)
    return False

print(givenSum(arr, target))
