
# WRITE THE CODE TO FIND SUM OF NUMBER TILL N


number = 4

def recursiveSum(num):
    if num == 0:
        return 0
    return recursiveSum(num-1)+num

print(recursiveSum(number))