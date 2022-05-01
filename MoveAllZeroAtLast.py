zeroArray = [10, 5, 0, 0, 4, 5, 6, 0]


def MoveAtLast(zeroArray):
    count = 0
    for i in range(len(zeroArray)):
        if zeroArray[i] != 0:
            print(count)
            zeroArray[i], zeroArray[count] = zeroArray[count], zeroArray[i]
            count += 1
    return zeroArray


print(MoveAtLast(zeroArray))
