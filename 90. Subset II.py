
nums = [1,2,2]
powerSet =[]
for i in range(1<<len(nums)):
    res = []
    for j in range(len(nums)):
        if i&(1 << j) == 0:
            print(nums[j], end="")
            res.extend([nums[j]])
    print()
    powerSet.append(res)
print(powerSet)