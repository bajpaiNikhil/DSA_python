
number = 234

def digitSum(num):
    if num == 0 :
        return 0
    return digitSum(num//10) + num%10

print(digitSum(number))