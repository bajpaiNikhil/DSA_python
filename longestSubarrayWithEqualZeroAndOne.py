arr = [1, 0, 1, 1, 1, 0, 0]


# do it again  .

# prefix_sum = [ 1 , ,2 ,3 ,4,4 ,4 ]
# modify_arr = [1 , -1 , 1, 1 ,1 -1 ,-1]
# modify_prefix_sum = [1, 0 , 1 ,2 ,3 ,2 ,1]
# prefix_sum_dict =  { 1:0 , 2:2 , 3: 3 ,4:4 }

def longestSumArrayOfZeroOne(arr):
    hashmap = {}
    currentMax = 0
    prefix_sum = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    print(arr)

    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum not in hashmap.keys():
            hashmap[prefix_sum] = i
        if prefix_sum in hashmap.keys():
            currentMax = max(currentMax, i - hashmap[prefix_sum])

    print(hashmap)
    return currentMax


print(longestSumArrayOfZeroOne(arr))
