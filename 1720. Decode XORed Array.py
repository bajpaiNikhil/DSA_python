encoded = [6,2,7,3]
first = 4

result = [first]
xor = first
for i in range(len(encoded)):
    xor^=encoded[i]
    result.append(xor)
print(result)
