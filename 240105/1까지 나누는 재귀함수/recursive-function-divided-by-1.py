def divide_to_one(num):
    print(num, end = " ")

    if num == 1:
        return 0

    if num % 2 == 0:
        num = num // 2

    else:
        num = num // 3
        
    divide_to_one(num)


num = int(input())
divide_to_one(num)