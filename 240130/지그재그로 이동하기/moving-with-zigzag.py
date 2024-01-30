# 입력 받기
A, B = map(int, input().split())

start = A
now = A
move = 1
direction = 1
movement = []
while True:
    if B in movement:
        break

    if direction > 0:
        for i in range(move):
            now += 1
            movement.append(now)

    else:
        for i in range(move):
            now -= 1
            movement.append(now)
 
    if move % 3 == 0:
        move *= 2
    else:
        move += 2
    
    direction *= -1

cnt = 0
for i in movement:
    cnt += 1
    if i == B:
        print(cnt)