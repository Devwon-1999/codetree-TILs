n = int(input())

box5 = n // 5

while box5 >= 0:
    remaining_capacity = n - (box5 * 5)
    if remaining_capacity % 3 == 0:
        box3 = remaining_capacity // 3
        result = box5 + box3
        print(result)
        break
    else:
        box5 -= 1

else:
    print(-1)