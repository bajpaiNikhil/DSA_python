rope = 23
a, b, c = 11, 9, 12


def ropeCut(rope, a, b, c):
    if rope == 0:
        return 0
    if rope < 0:
        return -1
    res = max(ropeCut(rope - a, a, b, c) , ropeCut(rope - b, a, b, c) , ropeCut(rope - c, a, b, c))

    if res == -1:
        return -1
    else:
        return res+1

print(ropeCut(rope, a, b, c))
