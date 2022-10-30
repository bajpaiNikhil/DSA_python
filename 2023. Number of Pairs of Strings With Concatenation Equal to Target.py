nums = [9,3,8,4,2,5,3,8,6,1]
average = []
for i in nums:
    if i&1 ==0:
        print(1)
        if i%3 ==0:
            average.append(i)
    else:
        print("odd")
print(sum(average)//len(average))
sum(average)//len(average) if len(average)>0 else 0


