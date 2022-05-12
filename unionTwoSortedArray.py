arr = [10, 20, 20]
brr = [5, 20, 40, 40]


def unionTwoSortedArray(arr, brr):
    i = 0
    j = 0
    res = []
    while i != len(arr) - 1 and j != len(brr) - 1:
        if i > 0 and arr[i] == arr[i - 1]:
            i += 1
        if j > 0 and brr[j] == brr[j - 1]:
            j += 1
        if arr[i] > brr[j]:
            res.append(brr[j])
            j += 1
        if arr[i] < brr[j]:
            res.append(arr[i])
            i += 1
        if arr[i] == brr[j]:
            res.append(arr[i])
            i += 1
            j += 1
    if i!=len(arr)-1:
        res.extend(arr[i:])
    if j!=len(brr)-1:
        res.extend(brr[j:])
    return res


print(unionTwoSortedArray(arr, brr))
