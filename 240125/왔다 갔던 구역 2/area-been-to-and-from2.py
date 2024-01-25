n = int(input())

now_place = 0

position_count = [0] * 2001  

for i in range(n):
    length, order = input().split()

    length = int(length)

    if order == "L":
        for i in range(now_place, now_place - length, -1):
            position_count[i] += 1
        now_place -= length  

    elif order == "R":
        for i in range(now_place, now_place + length):
            position_count[i] += 1
        now_place += length

answer = sum(1 for count in position_count if count >= 2)
print(answer)