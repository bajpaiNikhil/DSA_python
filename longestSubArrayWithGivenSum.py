arr = [8, 3, 1, 5, -6, 6, 2, 2]
target = 4

# arr = [1, -1, 1, 1, 1, -1, -1]
# target = 0

# prefix_sum  = [8 , 11 , 12 , 17 , 11 , 17 ,19,21 ]
# prefix_sum_dict = { 8:0 ,  11 : 1 , 12: 2 : 17:3 , 19: 6 , 21:7}
# arr = []
# arr = [5 ,8 ,-4, 9 , -2 , 2]

# arr = [5 ,8 ,-4 , -4, 9 , -2 , 2]
# prefix_Sum = [5 , 13 , 9 , 5 , 14 , 12 , 14 ]

# target =  0
# prefix_Sum  = [3 ,4 ,5 ,5 , 6 ,14 , 17 , 20 ]


def longestSubArrayGivenSum(arr, target):
    hashSet = {}
    prefix = 0
    current_longest = 0

    for i in range(len(arr)):
        prefix += arr[i]
        if prefix == target:
            return i + 1
        if prefix not in hashSet.keys():
            hashSet[prefix] = i
        if prefix - target in hashSet.keys():
            current_longest = max(current_longest, i - (hashSet[prefix - target]))
    return current_longest


print(longestSubArrayGivenSum(arr, target))
