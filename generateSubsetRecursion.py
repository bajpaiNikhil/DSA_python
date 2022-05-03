def generateSubset(s, current, index):
    if index == len(s):
        print(current)
        return
    generateSubset(s, current, index + 1)
    generateSubset(s, s[index] + current , index + 1)


s = "ABC"
print(generateSubset(s, current="", index=0))
