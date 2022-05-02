

number = 13

def convert(num):
    if num == 0:
        return
    convert(num//2)
    print(num%2)

convert(number)