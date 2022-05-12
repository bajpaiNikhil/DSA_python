arr = [3, 5, 10, 10, 10, 15, 15, 20]
brr = [5, 10, 10, 15, 30]


# o/p = 5 10 15

def intersectionSortedArray(arr, brr):
    i = 0
    j = 0
    res = []
    while i != len(arr)-1 and j != len(brr)-1:
        if i > 0 and arr[i] == arr[i - 1]:
            i += 1
            continue
        if j > 0 and brr[j] == brr[j - 1]:
            j += 1
            continue
        if arr[i]> brr[j]:
            j+=1
        if arr[i]<brr[j]:
            i+=1
        if arr[i] == brr[j]:
            res.append(arr[i])
            i+=1
            j+=1
    return res
print(intersectionSortedArray(arr , brr))
