array = [1,2,3,4,5,6,7]
d = 3
size = len(array)


def leftRotate(arrayIs, d, size):
    reverse(arrayIs, 0, d - 1)
    reverse(arrayIs, d, size - 1)
    reverse(arrayIs, 0, size - 1)
    return arrayIs


def reverse(arrayIs, low, high):
    while low < high:
        arrayIs[low], arrayIs[high] = arrayIs[high], arrayIs[low]
        low += 1
        high -= 1


print(leftRotate(array, d, size))
#time complexity is Thera(n)