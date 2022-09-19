nums = [5,1,6]

total = 0
for i in range(1<<len(nums)):
    current = 0
    for j in range(len(nums)):
        if (i & (1<<j)) >0:
            current^= nums[j]
    total+= current
print(total)




