nums = [3, 1, 3, 4, 2]

xor = 0
nums.sort()
for i in range(len(nums) - 1):
    xor = nums[i] ^ nums[i + 1]
    if xor == 0:
        print(nums[i])
    else:
        xor = 0
